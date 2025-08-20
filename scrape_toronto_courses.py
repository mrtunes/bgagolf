import requests
from bs4 import BeautifulSoup
import json
import re
import time
from typing import Dict, List, Optional

class TorontoCourseScraper:
    def __init__(self):
        self.base_url = "https://course.bluegolf.com/bluegolf/course/course/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def scrape_course(self, course_id: str) -> Optional[Dict]:
        """Scrape a specific course from bluegolf.com"""
        url = f"{self.base_url}{course_id}/detailedscorecard.htm"
        
        try:
            print(f"Scraping: {course_id}")
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"❌ Failed to fetch {course_id}: {response.status_code}")
                return None
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract course name from title
            course_name = self.extract_course_name(soup)
            if not course_name:
                print(f"❌ Could not extract course name from {course_id}")
                return None
            
            # Extract scorecard data
            scorecard_data = self.extract_scorecard_data(soup)
            if not scorecard_data:
                print(f"❌ Could not extract scorecard data from {course_id}")
                return None
                
            # Create course object
            course_obj = {
                'name': course_name,
                'location': 'Toronto, ON, Canada',  # All these courses are in Toronto
                'par': scorecard_data['par'],
                'yardage': scorecard_data['yardage'],
                'tee_info': scorecard_data.get('tee_info', 'Blue Tees'),
                'source': 'bluegolf.com',
                'url': url
            }
            
            print(f"✅ Successfully scraped: {course_name}")
            print(f"   Par: {sum(scorecard_data['par'])}, Yardage: {sum(scorecard_data['yardage'])}")
            
            return course_obj
            
        except Exception as e:
            print(f"❌ Error scraping {course_id}: {e}")
            return None
    
    def extract_course_name(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract course name from title"""
        title = soup.find('title')
        if title:
            title_text = title.get_text().strip()
            # Clean up BlueGolf title format
            course_name = title_text.replace(' - Detailed Scorecard | Course Database', '')
            course_name = course_name.replace('Detailed Scorecard', '').strip()
            if course_name and len(course_name) > 3:
                return course_name
        return None
    
    def extract_scorecard_data(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Extract scorecard data from BlueGolf table structure"""
        tables = soup.find_all('table')
        
        for table in tables:
            rows = table.find_all('tr')
            if len(rows) < 3:
                continue
            
            scorecard_data = self.parse_table(table)
            if scorecard_data:
                return scorecard_data
        
        return None
    
    def parse_table(self, table) -> Optional[Dict]:
        """Parse BlueGolf table format"""
        rows = table.find_all('tr')
        
        par_values = []
        yardage_values = []
        tee_info = "Blue Tees"
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if len(cells) < 20:  # Need at least hole data + totals
                continue
            
            cell_texts = [cell.get_text().strip() for cell in cells]
            
            # Look for par row
            if cell_texts[0].lower() == 'par':
                try:
                    par_candidates = cell_texts[1:19]  # Holes 1-18
                    par_values = [int(p) for p in par_candidates if p.isdigit()]
                    
                    if len(par_values) == 18 and all(3 <= p <= 5 for p in par_values):
                        print(f"   Found par: {par_values}")
                    else:
                        par_values = []
                except:
                    continue
            
            # Look for yardage row (try different tee types)
            elif cell_texts[0].lower() in ['yds', 'blue', 'white', 'red', 'black', 'gold']:
                try:
                    yardage_candidates = cell_texts[1:19]  # Holes 1-18
                    yardage_values = [int(y) for y in yardage_candidates if y.isdigit()]
                    
                    if len(yardage_values) == 18 and all(50 <= y <= 800 for y in yardage_values):
                        tee_info = f"{cell_texts[0].title()} Tees"
                        print(f"   Found yardage ({tee_info}): {yardage_values}")
                    else:
                        yardage_values = []
                except:
                    continue
        
        # Return if we have complete data
        if len(par_values) == 18 and len(yardage_values) == 18:
            return {
                'par': par_values,
                'yardage': yardage_values,
                'tee_info': tee_info
            }
        
        return None
    
    def create_safe_key(self, course_name: str) -> str:
        """Create a safe key for course storage"""
        safe_key = course_name.lower().replace(' ', '_')
        safe_key = re.sub(r'[^a-z0-9_]', '_', safe_key)
        safe_key = '_'.join(filter(None, safe_key.split('_')))
        return safe_key
    
    def update_javascript_file(self, new_courses: Dict, js_filename: str = 'script.js'):
        """Update JavaScript file with new courses"""
        try:
            # Read existing JavaScript file
            with open(js_filename, 'r') as f:
                js_content = f.read()
            
            # Load existing courses from JSON if available
            try:
                with open('all_courses.json', 'r') as f:
                    existing_courses = json.load(f)
            except:
                existing_courses = {}
            
            # Merge courses
            all_courses = {**existing_courses, **new_courses}
            
            # Find and replace the courses object in JavaScript
            start_marker = "const courses = {"
            start_idx = js_content.find(start_marker)
            if start_idx == -1:
                print("Could not find courses object in JavaScript file")
                return
            
            # Find the end of the courses object
            brace_count = 0
            end_idx = start_idx + len(start_marker)
            
            for i in range(start_idx + len(start_marker), len(js_content)):
                if js_content[i] == '{':
                    brace_count += 1
                elif js_content[i] == '}':
                    if brace_count == 0:
                        end_idx = i + 1
                        break
                    brace_count -= 1
            
            # Create new courses JavaScript object
            new_courses_js = "const courses = " + json.dumps(all_courses, indent=4) + ";"
            
            # Replace the courses object
            new_js_content = js_content[:start_idx] + new_courses_js + js_content[end_idx:]
            
            # Write back to file
            with open(js_filename, 'w') as f:
                f.write(new_js_content)
            
            # Save to JSON file
            with open('all_courses.json', 'w') as f:
                json.dump(all_courses, f, indent=2)
            
            print(f"\n✅ Updated {js_filename} with {len(all_courses)} total courses")
            
        except Exception as e:
            print(f"❌ Error updating JavaScript file: {e}")

def scrape_toronto_courses():
    """Scrape the three Toronto area courses"""
    scraper = TorontoCourseScraper()
    
    # Course IDs to scrape
    toronto_course_ids = [
        'ospreyvalleytoot',    # Osprey Valley
        'scarlettwoodsgc',     # Scarlettwoods Golf Course  
        'donvalleygc'          # Don Valley Golf Course
    ]
    
    scraped_courses = {}
    
    print("🏌️ Scraping Toronto area golf courses from BlueGolf.com...\n")
    
    for course_id in toronto_course_ids:
        print(f"📍 Scraping: {course_id}")
        course_data = scraper.scrape_course(course_id)
        
        if course_data:
            safe_key = scraper.create_safe_key(course_data['name'])
            scraped_courses[safe_key] = course_data
        
        # Be respectful with rate limiting
        print("   Waiting 2 seconds...\n")
        time.sleep(2)
    
    # Update JavaScript file with all new courses
    if scraped_courses:
        scraper.update_javascript_file(scraped_courses)
        
        print("🎉 SUCCESS! Scraped courses:")
        for key, course in scraped_courses.items():
            par_total = sum(course['par'])
            bga_total = par_total + 18
            print(f"   ✅ {course['name']} (Par {par_total}, BGA {bga_total})")
        
        print(f"\n📊 Added {len(scraped_courses)} new Toronto courses to the website!")
    else:
        print("😞 No courses were successfully scraped")

if __name__ == "__main__":
    scrape_toronto_courses()