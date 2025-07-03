import json

def add_oakdale_courses():
    """Add Oakdale Golf Course data extracted from scorecard images"""
    
    # Oakdale Course 1 & 3 (from oakdale-1-3.png)
    oakdale_1_3 = {
        "name": "Oakdale Golf & Country Club (Course 1 & 3)",
        "location": "Toronto, ON, Canada",
        "par": [4, 3, 4, 4, 3, 4, 4, 5, 5, 4, 3, 5, 4, 3, 4, 4, 4, 5],
        "yardage": [379, 188, 361, 374, 223, 330, 381, 492, 470, 281, 207, 553, 400, 186, 418, 398, 432, 479]
    }
    
    # Oakdale Course 1 & 2 (from oakdale1-2.png)  
    oakdale_1_2 = {
        "name": "Oakdale Golf & Country Club (Course 1 & 2)",
        "location": "Toronto, ON, Canada", 
        "par": [4, 3, 4, 4, 3, 4, 4, 5, 5, 4, 5, 3, 5, 3, 5, 4, 4, 3],
        "yardage": [379, 188, 361, 374, 223, 330, 381, 492, 470, 432, 545, 148, 590, 213, 560, 432, 354, 191]
    }
    
    oakdale_courses = {
        "oakdale_1_3": oakdale_1_3,
        "oakdale_1_2": oakdale_1_2
    }
    
    return oakdale_courses

def update_javascript_with_oakdale():
    """Update JavaScript file with Oakdale courses"""
    try:
        # Read existing JavaScript file
        with open('script.js', 'r') as f:
            js_content = f.read()
        
        # Get Oakdale courses
        oakdale_courses = add_oakdale_courses()
        
        # Find the courses object
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
        
        # Extract existing courses
        existing_courses_str = js_content[start_idx + len(start_marker) - 1:end_idx]
        
        # Parse existing courses (remove the outer braces and semicolon)
        existing_courses_str = existing_courses_str.strip()[1:-2]  # Remove { and };
        
        # Read existing courses from expanded_courses.json if it exists
        try:
            with open('expanded_courses.json', 'r') as f:
                existing_courses = json.load(f)
        except:
            existing_courses = {}
        
        # Merge with Oakdale courses
        all_courses = {**existing_courses, **oakdale_courses}
        
        # Create new courses JavaScript object
        new_courses_js = "const courses = " + json.dumps(all_courses, indent=4) + ";"
        
        # Replace the courses object
        new_js_content = js_content[:start_idx] + new_courses_js + js_content[end_idx:]
        
        # Write back to file
        with open('script.js', 'w') as f:
            f.write(new_js_content)
        
        # Also save to JSON file
        with open('all_courses.json', 'w') as f:
            json.dump(all_courses, f, indent=2)
        
        print(f"Updated script.js with {len(all_courses)} total courses")
        print("Added Oakdale courses:")
        for key, course in oakdale_courses.items():
            par_total = sum(course['par'])
            bogey_total = par_total + 18
            print(f"  - {course['name']} (Par {par_total}, Bogey {bogey_total})")
        
    except Exception as e:
        print(f"Error updating JavaScript file: {e}")

def main():
    print("Adding Oakdale Golf & Country Club courses from scorecard images...")
    update_javascript_with_oakdale()
    print("Complete! The courses are now available in the website.")

if __name__ == "__main__":
    main()