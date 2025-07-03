import requests
import json
import time
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class GolfCourseScraper:
    def __init__(self):
        self.base_url = "https://api.golfcourseapi.com"
        self.api_key = os.getenv('GOLF_API_KEY')  # Set this in environment
        self.courses_data = {}
        self.rate_limit_delay = 0.5  # 500ms between requests to be safe
        
    def get_course_data(self, course_id: str) -> Optional[Dict]:
        """Fetch course data from Golf Course API"""
        if not self.api_key:
            print("Error: GOLF_API_KEY environment variable not set")
            return None
            
        headers = {
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/courses/{course_id}", 
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error fetching course {course_id}: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Exception fetching course {course_id}: {e}")
            return None
    
    def search_courses(self, query: str = "", limit: int = 100) -> List[Dict]:
        """Search for courses"""
        if not self.api_key:
            print("Error: GOLF_API_KEY environment variable not set")
            return []
            
        headers = {
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        params = {
            'q': query,
            'limit': limit
        }
        
        # Try different possible endpoints
        endpoints = [
            f"{self.base_url}/courses/search",
            f"{self.base_url}/courses",
            f"{self.base_url}/search",
            f"{self.base_url}/api/courses/search",
            f"{self.base_url}/api/courses"
        ]
        
        for endpoint in endpoints:
            try:
                response = requests.get(endpoint, headers=headers, params=params)
                print(f"Trying endpoint: {endpoint} - Status: {response.status_code}")
                
                if response.status_code == 200:
                    return response.json().get('courses', response.json())
                elif response.status_code != 404:
                    print(f"Response: {response.text[:200]}")
                    
            except Exception as e:
                print(f"Exception with endpoint {endpoint}: {e}")
                continue
        
        return []
    
    def extract_course_info(self, course_data: Dict) -> Optional[Dict]:
        """Extract relevant course information and calculate bogey scores"""
        try:
            # Extract basic info
            name = course_data.get('name', 'Unknown Course')
            location = course_data.get('location', 'Unknown Location')
            
            # Extract scorecard data (assuming holes array exists)
            holes = course_data.get('holes', [])
            
            if len(holes) != 18:
                print(f"Skipping {name}: Does not have 18 holes ({len(holes)} holes)")
                return None
            
            # Extract par and yardage for each hole
            par_values = []
            yardages = []
            
            for hole in holes:
                par = hole.get('par')
                yardage = hole.get('yardage', 0)
                
                if par is None or par not in [3, 4, 5]:
                    print(f"Skipping {name}: Invalid par data")
                    return None
                    
                par_values.append(par)
                yardages.append(yardage)
            
            # Create course object
            course_obj = {
                'name': name,
                'location': location,
                'par': par_values,
                'yardage': yardages,
                'total_par': sum(par_values),
                'total_yardage': sum(yardages)
            }
            
            return course_obj
            
        except Exception as e:
            print(f"Error extracting course info: {e}")
            return None
    
    def scrape_courses(self, search_terms: List[str], max_courses: int = 50) -> Dict:
        """Scrape courses based on search terms"""
        all_courses = {}
        courses_scraped = 0
        
        for term in search_terms:
            if courses_scraped >= max_courses:
                break
                
            print(f"Searching for courses with term: {term}")
            
            # Search for courses
            search_results = self.search_courses(term, limit=20)
            
            for course_summary in search_results:
                if courses_scraped >= max_courses:
                    break
                    
                course_id = course_summary.get('id')
                if not course_id:
                    continue
                
                print(f"Fetching detailed data for: {course_summary.get('name', 'Unknown')}")
                
                # Get detailed course data
                course_data = self.get_course_data(course_id)
                
                if course_data:
                    # Extract and process course info
                    processed_course = self.extract_course_info(course_data)
                    
                    if processed_course:
                        # Create a safe key for the course
                        safe_key = self.create_safe_key(processed_course['name'])
                        all_courses[safe_key] = processed_course
                        courses_scraped += 1
                        print(f"Added course: {processed_course['name']} ({courses_scraped}/{max_courses})")
                
                # Rate limiting
                time.sleep(self.rate_limit_delay)
        
        return all_courses
    
    def create_safe_key(self, course_name: str) -> str:
        """Create a safe key for JavaScript from course name"""
        # Convert to lowercase, replace spaces and special chars with underscores
        safe_key = course_name.lower().replace(' ', '_')
        safe_key = ''.join(c if c.isalnum() or c == '_' else '_' for c in safe_key)
        # Remove multiple underscores
        safe_key = '_'.join(filter(None, safe_key.split('_')))
        return safe_key
    
    def save_to_json(self, courses_data: Dict, filename: str = 'courses.json'):
        """Save courses data to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(courses_data, f, indent=2)
            print(f"Saved {len(courses_data)} courses to {filename}")
        except Exception as e:
            print(f"Error saving to JSON: {e}")
    
    def update_javascript_file(self, courses_data: Dict, js_filename: str = 'script.js'):
        """Update the JavaScript file with new course data"""
        try:
            # Read existing JavaScript file
            with open(js_filename, 'r') as f:
                js_content = f.read()
            
            # Find the courses object and replace it
            start_marker = "const courses = {"
            end_marker = "};"
            
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
            new_courses_js = "const courses = " + json.dumps(courses_data, indent=4) + ";"
            
            # Replace the courses object
            new_js_content = js_content[:start_idx] + new_courses_js + js_content[end_idx:]
            
            # Write back to file
            with open(js_filename, 'w') as f:
                f.write(new_js_content)
            
            print(f"Updated {js_filename} with {len(courses_data)} courses")
            
        except Exception as e:
            print(f"Error updating JavaScript file: {e}")

def main():
    scraper = GolfCourseScraper()
    
    # Define search terms for different types of courses
    search_terms = [
        "pga tour",
        "championship",
        "country club",
        "resort",
        "municipal",
        "public",
        "golf course california",
        "golf course florida",
        "golf course texas",
        "golf course new york"
    ]
    
    print("Starting golf course scraping...")
    print("Make sure to set GOLF_API_KEY environment variable")
    print("Example: export GOLF_API_KEY='your_api_key_here'")
    
    # Scrape courses
    courses = scraper.scrape_courses(search_terms, max_courses=100)
    
    if courses:
        # Save to JSON
        scraper.save_to_json(courses, 'scraped_courses.json')
        
        # Update JavaScript file
        scraper.update_javascript_file(courses, 'script.js')
        
        print(f"Successfully scraped {len(courses)} courses!")
    else:
        print("No courses were scraped. Check your API key and connection.")

if __name__ == "__main__":
    main()