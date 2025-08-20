import json

def fix_scarlett_woods_course():
    """Fix Scarlett Woods Golf Club with correct course data"""
    
    # Correct Scarlett Woods data from Golf Canada and other sources
    # Par 61 Executive Course, 3,749 yards (White Tees)
    scarlett_woods_correct = {
        "name": "Scarlett Woods Golf Club",
        "location": "Toronto, ON, Canada",
        "par": [4, 3, 3, 3, 3, 3, 4, 3, 3, 3, 4, 4, 3, 4, 4, 3, 3, 4],  # Par 61 total
        "yardage": [309, 167, 230, 127, 107, 155, 353, 161, 182, 111, 262, 320, 118, 348, 255, 81, 155, 308],  # 3,749 yards total
        "tee_info": "White Tees",
        "source": "golfcanada.ca",
        "url": "https://www.golfcanada.ca/golf-facility/scarlett-woods-golf-club-en/",
        "course_type": "Executive Course",
        "note": "Par 61 executive course with mix of par 3s and par 4s"
    }
    
    # Verify the data
    total_par = sum(scarlett_woods_correct['par'])
    total_yardage = sum(scarlett_woods_correct['yardage'])
    
    print(f"Corrected Scarlett Woods Golf Club:")
    print(f"  Total Par: {total_par}")
    print(f"  Total Yardage: {total_yardage}")
    print(f"  Course Type: Executive Course")
    print(f"  Par breakdown: {scarlett_woods_correct['par']}")
    print(f"  Par 3s: {scarlett_woods_correct['par'].count(3)} holes")
    print(f"  Par 4s: {scarlett_woods_correct['par'].count(4)} holes")
    print()
    
    return {"scarlett_woods_golf_club": scarlett_woods_correct}

def update_javascript_with_corrected_scarlett_woods():
    """Update JavaScript file with corrected Scarlett Woods data"""
    try:
        # Read existing JavaScript file
        with open('script.js', 'r') as f:
            js_content = f.read()
        
        # Load existing courses from JSON
        try:
            with open('all_courses.json', 'r') as f:
                existing_courses = json.load(f)
        except:
            existing_courses = {}
        
        # Get corrected Scarlett Woods data
        corrected_course = fix_scarlett_woods_course()
        
        # Update the existing courses with corrected data
        existing_courses.update(corrected_course)
        
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
        new_courses_js = "const courses = " + json.dumps(existing_courses, indent=4) + ";"
        
        # Replace the courses object
        new_js_content = js_content[:start_idx] + new_courses_js + js_content[end_idx:]
        
        # Write back to file
        with open('script.js', 'w') as f:
            f.write(new_js_content)
        
        # Save to JSON file
        with open('all_courses.json', 'w') as f:
            json.dump(existing_courses, f, indent=2)
        
        print(f"✅ Updated script.js with {len(existing_courses)} total courses")
        print("✅ Fixed Scarlett Woods Golf Club data:")
        
        course = corrected_course["scarlett_woods_golf_club"]
        par_total = sum(course['par'])
        bga_total = par_total + 18
        print(f"   - {course['name']} (Par {par_total}, BGA {bga_total})")
        print(f"   - Executive course with {course['par'].count(3)} par 3s and {course['par'].count(4)} par 4s")
        
    except Exception as e:
        print(f"❌ Error updating JavaScript file: {e}")

def main():
    print("🔧 Fixing Scarlett Woods Golf Club with correct course data...\n")
    update_javascript_with_corrected_scarlett_woods()
    print("\n🎉 Complete! Scarlett Woods now has the correct Par 61 executive course data.")

if __name__ == "__main__":
    main()