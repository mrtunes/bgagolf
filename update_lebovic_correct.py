import json

def update_lebovic_with_correct_data():
    """Update Lebovic Golf Club with actual scorecard data from research"""
    
    # Actual Lebovic Golf Club data from 18Birdies and other sources
    # Par 70 Championship Course, 6,414 yards (Black Tees)
    lebovic_golf_correct = {
        "name": "Lebovic Golf Club",
        "location": "Aurora, ON, Canada",
        # Par breakdown: Front 9 = Par 36, Back 9 = Par 34, Total = Par 70
        "par": [5, 4, 5, 4, 3, 4, 4, 4, 3, 5, 4, 4, 3, 4, 3, 4, 3, 4],  # Par 70 total
        # Black Tees yardages: Front 9 = 3,206 yards, Back 9 = 3,208 yards, Total = 6,414 yards
        "yardage": [523, 416, 546, 322, 131, 385, 373, 330, 180, 563, 408, 397, 181, 453, 170, 409, 185, 442],  # 6,414 yards total
        "tee_info": "Black Tees",
        "source": "18birdies.com and course research",
        "url": "https://18birdies.com/golf-courses/club/d0d21190-af72-11e7-9f6b-0680a328ea36/lebovic-golf-club",
        "course_type": "Championship Course",
        "designer": "Doug Carrick",
        "opened": "2015",
        "note": "Par 70 championship course built on Oak Ridges Moraine",
        "features": "Unique tunnel connects holes on each side of Leslie Street"
    }
    
    # Verify the correct data
    total_par = sum(lebovic_golf_correct['par'])
    total_yardage = sum(lebovic_golf_correct['yardage'])
    
    print(f"Corrected Lebovic Golf Club Data:")
    print(f"  Total Par: {total_par}")
    print(f"  Total Yardage: {total_yardage}")
    print(f"  Par 3s: {lebovic_golf_correct['par'].count(3)} holes")
    print(f"  Par 4s: {lebovic_golf_correct['par'].count(4)} holes")
    print(f"  Par 5s: {lebovic_golf_correct['par'].count(5)} holes")
    print(f"  Designer: {lebovic_golf_correct['designer']}")
    print(f"  Opened: {lebovic_golf_correct['opened']}")
    print()
    
    return {"lebovic_golf_club": lebovic_golf_correct}

def update_javascript_with_correct_lebovic():
    """Update JavaScript file with corrected Lebovic Golf Club data"""
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
        
        # Get corrected Lebovic data
        corrected_course = update_lebovic_with_correct_data()
        
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
        print("✅ Fixed Lebovic Golf Club data:")
        
        course = corrected_course["lebovic_golf_club"]
        par_total = sum(course['par'])
        bga_total = par_total + 18
        print(f"   - {course['name']} (Par {par_total}, BGA {bga_total})")
        print(f"   - Championship course by Doug Carrick")
        print(f"   - {course['par'].count(3)} par 3s, {course['par'].count(4)} par 4s, {course['par'].count(5)} par 5s")
        
    except Exception as e:
        print(f"❌ Error updating JavaScript file: {e}")

def main():
    print("🔧 Updating Lebovic Golf Club with correct championship course data...\n")
    update_javascript_with_correct_lebovic()
    print("\n🎉 Complete! Lebovic Golf Club now has the correct Par 70 championship data.")

if __name__ == "__main__":
    main()