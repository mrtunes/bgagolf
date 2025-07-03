import requests
from bs4 import BeautifulSoup
import json
import re
import time
from typing import Dict, List, Optional

class BlueGolfScraperV2:
    def __init__(self):
        self.base_url = "https://course.bluegolf.com/bluegolf/course/course/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def scrape_course(self, course_id: str) -> Optional[Dict]:
        """Scrape a specific course from bluegolf.com"""
        url = f"{self.base_url}{course_id}/detailedscorecard.htm"
        
        try:
            print(f"Scraping: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"Failed to fetch {url}: {response.status_code}")
                return None
                
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract course name from title
            course_name = self.extract_course_name(soup)
            if not course_name:
                print(f"Could not extract course name from {url}")
                return None
            
            # Extract scorecard data from the specific BlueGolf table structure
            scorecard_data = self.extract_bluegolf_scorecard_data(soup)
            if not scorecard_data:
                print(f"Could not extract scorecard data from {url}")
                return None
                
            # Create course object
            course_obj = {
                'name': course_name,
                'location': self.extract_location(soup),
                'par': scorecard_data['par'],
                'yardage': scorecard_data['yardage'],
                'tee_info': scorecard_data.get('tee_info', 'Blue Tees'),
                'source': 'bluegolf.com',
                'url': url
            }
            
            return course_obj
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
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
    
    def extract_location(self, soup: BeautifulSoup) -> str:
        """Extract location from BlueGolf page"""
        # BlueGolf pages often have location info in specific patterns
        text = soup.get_text().lower()
        
        # Look for common location patterns
        location_patterns = [
            r'([A-Z][a-z]+,\s*[A-Z]{2})',  # City, State
            r'([A-Z][a-z]+,\s*[A-Z][a-z]+)',  # City, Province
        ]
        
        for pattern in location_patterns:
            match = re.search(pattern, soup.get_text())
            if match:
                return match.group(1)
        
        return "Location Unknown"
    
    def extract_bluegolf_scorecard_data(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Extract scorecard data using BlueGolf's specific table structure"""
        tables = soup.find_all('table')
        
        # Based on our analysis, BlueGolf has tables with this structure:
        # Row 1: Tee | 1 | 2 | 3 | ... | 18 | In | Tot
        # Row 2: yds | yardages for each hole
        # Row 3: Par | par for each hole
        
        for table in tables:
            rows = table.find_all('tr')
            if len(rows) < 3:
                continue
            
            # Look for a table that has the right structure
            scorecard_data = self.parse_bluegolf_table(table)
            if scorecard_data:
                return scorecard_data
        
        return None
    
    def parse_bluegolf_table(self, table) -> Optional[Dict]:
        """Parse BlueGolf's specific table format"""
        rows = table.find_all('tr')
        
        par_values = []
        yardage_values = []
        tee_info = "Unknown Tees"
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if len(cells) < 20:  # Need at least hole data + totals
                continue
            
            # Get text from all cells
            cell_texts = [cell.get_text().strip() for cell in cells]
            
            # Check if this is a par row
            if cell_texts[0].lower() == 'par':
                # Extract par values for holes 1-18 (skip first cell and last 2 cells which are totals)
                try:
                    par_candidates = cell_texts[1:19]  # Holes 1-18
                    par_values = [int(p) for p in par_candidates if p.isdigit()]
                    
                    # Validate par values
                    if len(par_values) == 18 and all(3 <= p <= 5 for p in par_values):
                        print(f"Found par values: {par_values}")
                    else:
                        par_values = []
                except:
                    continue
            
            # Check if this is a yardage row
            elif cell_texts[0].lower() in ['yds', 'blue', 'white', 'red', 'black', 'gold']:
                try:
                    yardage_candidates = cell_texts[1:19]  # Holes 1-18
                    yardage_values = [int(y) for y in yardage_candidates if y.isdigit()]
                    
                    # Validate yardage values
                    if len(yardage_values) == 18 and all(50 <= y <= 800 for y in yardage_values):
                        tee_info = f"{cell_texts[0].title()} Tees"
                        print(f"Found yardage values for {tee_info}: {yardage_values}")
                    else:
                        yardage_values = []
                except:
                    continue
        
        # Return data if we have both par and yardage
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
            
            print(f"Updated {js_filename} with {len(all_courses)} total courses")
            
        except Exception as e:
            print(f"Error updating JavaScript file: {e}")

def test_humber_valley_v2():
    """Test the improved scraper on Humber Valley"""
    scraper = BlueGolfScraperV2()
    
    course_data = scraper.scrape_course('humbervalleygc')
    
    if course_data:
        print("\n✅ Successfully scraped course:")
        print(f"Name: {course_data['name']}")
        print(f"Location: {course_data['location']}")
        print(f"Tees: {course_data['tee_info']}")
        print(f"Par: {course_data['par']}")
        print(f"Total Par: {sum(course_data['par'])}")
        print(f"Yardage: {course_data['yardage']}")
        print(f"Total Yardage: {sum(course_data['yardage'])}")
        
        # Save to JavaScript
        safe_key = scraper.create_safe_key(course_data['name'])
        courses = {safe_key: course_data}
        scraper.update_javascript_file(courses)
        
        print(f"\n🎉 Course added to website as '{safe_key}'")
        
    else:
        print("❌ Failed to scrape course data")

if __name__ == "__main__":
    print("Testing improved BlueGolf scraper...")
    test_humber_valley_v2()