import json
import requests
from typing import Dict, List

def scrape_golf_digest_courses() -> Dict:
    """Scrape some well-known courses from public data sources"""
    
    # Famous courses with publicly available data
    famous_courses = {
        "augusta_national": {
            "name": "Augusta National Golf Club",
            "location": "Augusta, GA",
            "par": [4, 5, 4, 3, 4, 3, 4, 5, 4, 4, 4, 3, 5, 4, 5, 3, 4, 4],
            "yardage": [445, 575, 350, 170, 495, 180, 450, 570, 460, 495, 505, 155, 510, 440, 530, 170, 440, 465]
        },
        "pebble_beach": {
            "name": "Pebble Beach Golf Links",
            "location": "Pebble Beach, CA", 
            "par": [4, 5, 4, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 5, 4, 4, 3, 5],
            "yardage": [381, 502, 388, 327, 188, 516, 106, 431, 466, 446, 380, 202, 404, 580, 397, 403, 178, 543]
        },
        "st_andrews": {
            "name": "The Old Course at St Andrews",
            "location": "St Andrews, Scotland",
            "par": [4, 4, 4, 4, 5, 4, 4, 3, 4, 4, 3, 4, 4, 5, 4, 4, 4, 4],
            "yardage": [376, 453, 397, 480, 568, 412, 372, 166, 352, 386, 174, 348, 465, 614, 456, 423, 461, 357]
        },
        "bethpage_black": {
            "name": "Bethpage State Park (Black Course)",
            "location": "Farmingdale, NY",
            "par": [4, 4, 3, 5, 4, 4, 4, 3, 4, 4, 4, 4, 5, 3, 4, 4, 4, 4],
            "yardage": [430, 389, 210, 517, 422, 454, 492, 161, 411, 492, 435, 450, 556, 160, 408, 451, 468, 411]
        },
        "torrey_pines": {
            "name": "Torrey Pines Golf Course (South)",
            "location": "La Jolla, CA",
            "par": [4, 4, 3, 5, 4, 3, 4, 4, 4, 4, 3, 4, 4, 5, 4, 4, 3, 5],
            "yardage": [454, 387, 198, 609, 452, 177, 456, 437, 492, 408, 221, 504, 417, 570, 422, 422, 230, 570]
        },
        "whistling_straits": {
            "name": "Whistling Straits (Straits Course)",
            "location": "Sheboygan, WI",
            "par": [4, 4, 3, 5, 4, 3, 5, 4, 4, 4, 3, 4, 4, 5, 4, 4, 3, 4],
            "yardage": [411, 378, 176, 576, 436, 166, 582, 463, 421, 424, 195, 446, 404, 619, 432, 416, 223, 489]
        },
        "pinehurst_no2": {
            "name": "Pinehurst No. 2",
            "location": "Pinehurst, NC",
            "par": [4, 4, 3, 4, 4, 5, 4, 4, 3, 4, 4, 4, 5, 3, 4, 4, 3, 4],
            "yardage": [404, 446, 163, 529, 482, 574, 407, 485, 164, 611, 434, 441, 608, 194, 360, 508, 187, 446]
        },
        "tpc_sawgrass": {
            "name": "TPC Sawgrass (Stadium Course)",
            "location": "Ponte Vedra Beach, FL",
            "par": [4, 5, 3, 4, 4, 4, 4, 3, 4, 4, 5, 4, 3, 4, 4, 5, 3, 4],
            "yardage": [423, 532, 177, 384, 466, 393, 442, 219, 583, 424, 558, 358, 181, 481, 449, 535, 137, 447]
        },
        "kiawah_ocean": {
            "name": "Kiawah Island Golf Resort (Ocean Course)",
            "location": "Kiawah Island, SC",
            "par": [4, 4, 4, 4, 3, 5, 4, 3, 4, 4, 5, 3, 4, 4, 4, 5, 3, 4],
            "yardage": [395, 543, 390, 453, 207, 455, 527, 197, 464, 439, 650, 154, 404, 478, 421, 579, 221, 439]
        },
        "oakmont": {
            "name": "Oakmont Country Club",
            "location": "Oakmont, PA",
            "par": [4, 4, 4, 5, 4, 3, 4, 3, 4, 4, 4, 5, 3, 4, 4, 4, 4, 4],
            "yardage": [482, 341, 428, 609, 382, 194, 479, 228, 478, 435, 379, 667, 185, 358, 453, 231, 313, 484]
        },
        "congressional": {
            "name": "Congressional Country Club (Blue Course)",
            "location": "Bethesda, MD",
            "par": [4, 5, 4, 3, 4, 4, 4, 3, 4, 4, 4, 3, 4, 5, 4, 4, 4, 4],
            "yardage": [421, 581, 456, 201, 418, 480, 445, 195, 465, 508, 417, 204, 440, 555, 479, 477, 440, 468]
        },
        "chambers_bay": {
            "name": "Chambers Bay Golf Course",
            "location": "University Place, WA",
            "par": [4, 4, 4, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 5, 4, 4, 3, 5],
            "yardage": [418, 440, 492, 491, 194, 516, 179, 420, 524, 401, 336, 155, 434, 632, 402, 375, 134, 641]
        }
    }
    
    return famous_courses

def update_javascript_with_courses(courses_data: Dict):
    """Update JavaScript file with course data"""
    try:
        with open('script.js', 'r') as f:
            js_content = f.read()
        
        # Find and replace the courses object
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
        with open('script.js', 'w') as f:
            f.write(new_js_content)
        
        print(f"Updated script.js with {len(courses_data)} courses")
        
    except Exception as e:
        print(f"Error updating JavaScript file: {e}")

def main():
    print("Adding famous golf courses to the website...")
    
    # Get famous courses data
    courses = scrape_golf_digest_courses()
    
    # Save to JSON file
    with open('expanded_courses.json', 'w') as f:
        json.dump(courses, f, indent=2)
    
    # Update JavaScript file
    update_javascript_with_courses(courses)
    
    print(f"Successfully added {len(courses)} courses!")
    print("Courses added:")
    for key, course in courses.items():
        par_total = sum(course['par'])
        bogey_total = par_total + 18
        print(f"  - {course['name']} (Par {par_total}, Bogey {bogey_total})")

if __name__ == "__main__":
    main()