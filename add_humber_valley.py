import json

def add_humber_valley_manually():
    """Add Humber Valley Golf Club manually based on the scraped data"""
    
    # Based on the page inspection, we have the exact data:
    # Par: 4 4 4 3 4 3 4 4 4 4 4 4 4 4 3 5 5 3 (Total: 70)
    # Blue Tees Yardage: 348 364 249 127 311 89 316 306 325 339 314 296 301 366 167 515 516 197 (Total: 5446)
    
    humber_valley = {
        "name": "Humber Valley Golf Club",
        "location": "Toronto, ON, Canada",
        "par": [4, 4, 4, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 5, 5, 3],
        "yardage": [348, 364, 249, 127, 311, 89, 316, 306, 325, 339, 314, 296, 301, 366, 167, 515, 516, 197],
        "tee_info": "Blue Tees",
        "source": "bluegolf.com",
        "url": "https://course.bluegolf.com/bluegolf/course/course/humbervalleygc/detailedscorecard.htm"
    }
    
    # Verify the data
    total_par = sum(humber_valley['par'])
    total_yardage = sum(humber_valley['yardage'])
    
    print(f"Course: {humber_valley['name']}")
    print(f"Location: {humber_valley['location']}")
    print(f"Total Par: {total_par}")
    print(f"Total Yardage: {total_yardage}")
    print(f"Par values: {humber_valley['par']}")
    print(f"Yardage values: {humber_valley['yardage']}")
    
    return {"humber_valley_golf_club": humber_valley}

def update_javascript_with_humber_valley():
    """Update JavaScript file with Humber Valley course"""
    try:
        # Read existing JavaScript file
        with open('script.js', 'r') as f:
            js_content = f.read()
        
        # Get Humber Valley course
        humber_valley_courses = add_humber_valley_manually()
        
        # Load existing courses from JSON if available
        try:
            with open('all_courses.json', 'r') as f:
                existing_courses = json.load(f)
        except:
            existing_courses = {}
        
        # Merge with Humber Valley course
        all_courses = {**existing_courses, **humber_valley_courses}
        
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
        print("Added Humber Valley Golf Club:")
        for key, course in humber_valley_courses.items():
            par_total = sum(course['par'])
            bga_total = par_total + 18
            print(f"  - {course['name']} (Par {par_total}, BGA {bga_total})")
        
    except Exception as e:
        print(f"Error updating JavaScript file: {e}")

def main():
    print("Adding Humber Valley Golf Club from BlueGolf.com...")
    update_javascript_with_humber_valley()
    print("Complete! Humber Valley Golf Club is now available in the website.")

if __name__ == "__main__":
    main()