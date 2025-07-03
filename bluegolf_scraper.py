import requests
from bs4 import BeautifulSoup
import json
import re
import time
from typing import Dict, List, Optional

class BlueGolfScraper:
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
            
            # Extract course name
            course_name = self.extract_course_name(soup)
            if not course_name:
                print(f"Could not extract course name from {url}")
                return None
            
            # Extract scorecard data
            scorecard_data = self.extract_scorecard_data(soup)
            if not scorecard_data:
                print(f"Could not extract scorecard data from {url}")
                return None
                
            # Create course object
            course_obj = {
                'name': course_name,
                'location': self.extract_location(soup, course_name),
                'par': scorecard_data['par'],
                'yardage': scorecard_data['yardage'],
                'source': 'bluegolf.com',
                'url': url
            }
            
            return course_obj
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None
    
    def extract_course_name(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract course name from various possible locations"""
        # Try different selectors for course name
        selectors = [
            'title',
            'h1',
            'h2',
            '.course-name',
            '.courseName',
            '#courseName'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                text = element.get_text().strip()
                # Clean up title text
                if 'scorecard' in text.lower():
                    text = re.sub(r'\s*-?\s*scorecard.*$', '', text, flags=re.IGNORECASE)
                if text and len(text) > 3:
                    return text
        
        return None
    
    def extract_location(self, soup: BeautifulSoup, course_name: str) -> str:
        """Extract or infer location information"""
        # Try to find location info
        location_selectors = [
            '.location',
            '.address',
            '.course-location'
        ]
        
        for selector in location_selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text().strip()
        
        # If no location found, return default
        return "Location Unknown"
    
    def extract_scorecard_data(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Extract par and yardage data from scorecard table"""
        # BlueGolf specific: look for the main scorecard table
        # Try multiple approaches to find the scorecard data
        
        # Method 1: Look for tables with specific classes or IDs
        scorecard_table = soup.find('table', {'class': re.compile(r'scorecard|course', re.I)})
        if not scorecard_table:
            scorecard_table = soup.find('table', {'id': re.compile(r'scorecard|course', re.I)})
        
        # Method 2: Look for any table with enough columns (18+ holes)
        if not scorecard_table:
            tables = soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                if len(rows) >= 3:  # Need at least hole numbers, par, and yardage
                    # Check if any row has 18+ cells (holes 1-18)
                    for row in rows:
                        cells = row.find_all(['td', 'th'])
                        if len(cells) >= 18:
                            scorecard_table = table
                            break
                if scorecard_table:
                    break
        
        if scorecard_table:
            scorecard_data = self.parse_scorecard_table(scorecard_table)
            if scorecard_data:
                return scorecard_data
        
        # Method 3: Try to parse any structured data we can find
        return self.extract_data_alternative_method(soup)
    
    def parse_scorecard_table(self, table) -> Optional[Dict]:
        """Parse a scorecard table to extract par and yardage"""
        rows = table.find_all('tr')
        
        par_values = []
        yardage_values = []
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if len(cells) < 18:  # Need at least 18 holes worth of data
                continue
            
            # Extract text from cells
            cell_texts = [cell.get_text().strip() for cell in cells]
            
            # Look for par row
            if self.is_par_row(cell_texts):
                par_values = self.extract_numeric_values(cell_texts[1:19])  # Skip first cell (label)
                
            # Look for yardage row (usually the longest numbers)
            elif self.is_yardage_row(cell_texts):
                yardage_values = self.extract_numeric_values(cell_texts[1:19])
        
        # Validate we have complete data
        if len(par_values) == 18 and len(yardage_values) == 18:
            # Validate par values are reasonable (3-5)
            if all(3 <= p <= 5 for p in par_values):
                return {
                    'par': par_values,
                    'yardage': yardage_values
                }
        
        return None
    
    def is_par_row(self, cell_texts: List[str]) -> bool:
        """Check if this row contains par data"""
        first_cell = cell_texts[0].lower()
        return 'par' in first_cell
    
    def is_yardage_row(self, cell_texts: List[str]) -> bool:
        """Check if this row contains yardage data"""
        first_cell = cell_texts[0].lower()
        # Look for common yardage indicators
        yardage_indicators = ['yard', 'yds', 'distance', 'blue', 'white', 'red', 'black', 'gold']
        return any(indicator in first_cell for indicator in yardage_indicators)
    
    def extract_numeric_values(self, texts: List[str]) -> List[int]:
        """Extract numeric values from text list"""
        values = []
        for text in texts:
            # Extract numbers from text
            numbers = re.findall(r'\d+', text)
            if numbers:
                values.append(int(numbers[0]))
            else:
                values.append(0)  # Default for missing data
        return values
    
    def extract_data_alternative_method(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Alternative method to extract scorecard data if table parsing fails"""
        # Look for any text patterns that might contain scorecard data
        text = soup.get_text()
        
        # Try to find par values in the text
        par_pattern = r'Par[:\s]*(\d+(?:\s+\d+){17})'
        par_match = re.search(par_pattern, text, re.IGNORECASE)
        
        if par_match:
            par_values = [int(x) for x in par_match.group(1).split()]
            if len(par_values) == 18 and all(3 <= p <= 5 for p in par_values):
                # Try to find corresponding yardage values
                yardage_pattern = r'(?:Yard|Distance|Blue|White|Red)[:\s]*(\d+(?:\s+\d+){17})'
                yardage_match = re.search(yardage_pattern, text, re.IGNORECASE)
                
                if yardage_match:
                    yardage_values = [int(x) for x in yardage_match.group(1).split()]
                    if len(yardage_values) == 18:
                        return {
                            'par': par_values,
                            'yardage': yardage_values
                        }
        
        return None
    
    def create_safe_key(self, course_name: str) -> str:
        """Create a safe key for course storage"""
        safe_key = course_name.lower().replace(' ', '_')
        safe_key = ''.join(c if c.isalnum() or c == '_' else '_' for c in safe_key)
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

def test_humber_valley():
    """Test scraping Humber Valley Golf Course"""
    scraper = BlueGolfScraper()
    
    # Test with the provided URL
    course_data = scraper.scrape_course('humbervalleygc')
    
    if course_data:
        print("Successfully scraped course:")
        print(f"Name: {course_data['name']}")
        print(f"Location: {course_data['location']}")
        print(f"Par: {course_data['par']}")
        print(f"Total Par: {sum(course_data['par'])}")
        print(f"Yardage: {course_data['yardage']}")
        print(f"Total Yardage: {sum(course_data['yardage'])}")
        
        # Save to JavaScript
        safe_key = scraper.create_safe_key(course_data['name'])
        courses = {safe_key: course_data}
        scraper.update_javascript_file(courses)
        
    else:
        print("Failed to scrape course data")

def scrape_multiple_bluegolf_courses():
    """Scrape multiple courses from bluegolf.com"""
    scraper = BlueGolfScraper()
    
    # List of course IDs to try (these would need to be discovered)
    course_ids = [
        'humbervalleygc',
        # Add more course IDs here as discovered
    ]
    
    scraped_courses = {}
    
    for course_id in course_ids:
        print(f"\nScraping course: {course_id}")
        course_data = scraper.scrape_course(course_id)
        
        if course_data:
            safe_key = scraper.create_safe_key(course_data['name'])
            scraped_courses[safe_key] = course_data
            print(f"✅ Successfully scraped: {course_data['name']}")
        else:
            print(f"❌ Failed to scrape: {course_id}")
        
        # Be respectful with rate limiting
        time.sleep(2)
    
    if scraped_courses:
        # Update JavaScript file with all new courses
        scraper = BlueGolfScraper()
        scraper.update_javascript_file(scraped_courses)
        print(f"\n🎉 Successfully scraped {len(scraped_courses)} courses!")
    else:
        print("\n😞 No courses were successfully scraped")

if __name__ == "__main__":
    print("Testing BlueGolf scraper with Humber Valley Golf Course...")
    test_humber_valley()