import json

def add_toronto_courses_manually():
    """Add Toronto courses manually based on the scraped data inspection"""
    
    # From the page inspection, I can extract the exact data:
    
    # TPC Toronto at Osprey Valley - North (Blue Tees)
    # Par: 5 4 4 3 4 4 3 5 4 4 3 4 5 3 4 4 4 5 (Total: 72)
    # Blue Tees: 496 428 376 140 402 312 170 494 388 370 149 328 514 144 338 420 416 494 (Total: 6379)
    
    osprey_valley = {
        "name": "TPC Toronto at Osprey Valley - North",
        "location": "Toronto, ON, Canada",
        "par": [5, 4, 4, 3, 4, 4, 3, 5, 4, 4, 3, 4, 5, 3, 4, 4, 4, 5],
        "yardage": [496, 428, 376, 140, 402, 312, 170, 494, 388, 370, 149, 328, 514, 144, 338, 420, 416, 494],
        "tee_info": "Blue Tees",
        "source": "bluegolf.com",
        "url": "https://course.bluegolf.com/bluegolf/course/course/ospreyvalleytoot/detailedscorecard.htm"
    }
    
    # Scarlett Woods Golf Club (Temporary Tees)
    # Par: 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 (Total: 72)
    # Note: This appears to be temporary/placeholder data with 100 yards each hole
    # This is likely a driving range or temporary setup, but we'll include it
    scarlett_woods = {
        "name": "Scarlett Woods Golf Club",
        "location": "Toronto, ON, Canada", 
        "par": [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        "yardage": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        "tee_info": "Temporary Tees",
        "source": "bluegolf.com",
        "url": "https://course.bluegolf.com/bluegolf/course/course/scarlettwoodsgc/detailedscorecard.htm",
        "note": "Appears to be temporary/practice course setup"
    }
    
    # Don Valley Golf Club (Blue Tees)
    # Par: 4 4 5 4 3 5 3 5 4 4 4 5 3 4 3 4 4 4 (Total: 72)
    # Blue Tees: 329 464 502 429 177 540 164 525 292 320 345 490 152 375 138 305 291 325 (Total: 6163)
    don_valley = {
        "name": "Don Valley Golf Club",
        "location": "Toronto, ON, Canada",
        "par": [4, 4, 5, 4, 3, 5, 3, 5, 4, 4, 4, 5, 3, 4, 3, 4, 4, 4],
        "yardage": [329, 464, 502, 429, 177, 540, 164, 525, 292, 320, 345, 490, 152, 375, 138, 305, 291, 325],
        "tee_info": "Blue Tees",
        "source": "bluegolf.com", 
        "url": "https://course.bluegolf.com/bluegolf/course/course/donvalleygc/detailedscorecard.htm"
    }
    
    # Verify the data
    courses = {
        "tpc_toronto_osprey_valley_north": osprey_valley,
        "scarlett_woods_golf_club": scarlett_woods,
        "don_valley_golf_club": don_valley
    }
    
    for key, course in courses.items():
        total_par = sum(course['par'])
        total_yardage = sum(course['yardage'])
        print(f"Course: {course['name']}")
        print(f"  Total Par: {total_par}")
        print(f"  Total Yardage: {total_yardage}")
        print(f"  Par values: {course['par']}")
        print()
    
    return courses

def update_javascript_with_toronto_courses():
    """Update JavaScript file with Toronto courses"""
    try:
        # Read existing JavaScript file
        with open('script.js', 'r') as f:
            js_content = f.read()
        
        # Get Toronto courses
        toronto_courses = add_toronto_courses_manually()
        
        # Load existing courses from JSON if available
        try:
            with open('all_courses.json', 'r') as f:
                existing_courses = json.load(f)
        except:
            existing_courses = {}
        
        # Merge with Toronto courses
        all_courses = {**existing_courses, **toronto_courses}
        
        # Find and replace the courses object
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
        with open('script.js', 'w') as f:
            f.write(new_js_content)
        
        # Save to JSON file
        with open('all_courses.json', 'w') as f:
            json.dump(all_courses, f, indent=2)
        
        print(f"Updated script.js with {len(all_courses)} total courses")
        print("\nAdded Toronto courses:")
        for key, course in toronto_courses.items():
            par_total = sum(course['par'])
            bga_total = par_total + 18
            print(f"  ✅ {course['name']} (Par {par_total}, BGA {bga_total})")
        
    except Exception as e:
        print(f"Error updating JavaScript file: {e}")

def main():
    print("🏌️ Adding Toronto golf courses from BlueGolf.com...\n")
    update_javascript_with_toronto_courses()
    print("\n🎉 Complete! Toronto courses are now available in the website.")
    print("\nNote: Scarlett Woods appears to have temporary/placeholder data.")

if __name__ == "__main__":
    main()