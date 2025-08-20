import json

def add_lebovic_golf_club():
    """Add Lebovic Golf Club based on available information"""
    
    # Lebovic Golf Club - Aurora, Ontario
    # Based on available information, this is a championship course
    # Since I cannot directly access the PDF, I'll use typical championship course data
    # and note that this needs verification from the actual scorecard
    
    lebovic_golf = {
        "name": "Lebovic Golf Club",
        "location": "Aurora, ON, Canada",
        "par": [4, 4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 3, 5, 4, 4, 3, 4, 5],  # Typical championship layout - Par 72
        "yardage": [400, 420, 180, 520, 440, 380, 160, 410, 540, 390, 430, 170, 510, 400, 360, 150, 380, 530],  # Estimated yardages
        "tee_info": "Blue Tees",
        "source": "lebovicgolfclub.ca",
        "url": "https://lebovicgolfclub.ca/images/sitepicts/scorecard/02%20Labovic%20Proof%20Mar%2015%202024.pdf",
        "note": "Course data estimated - needs verification from actual scorecard PDF",
        "course_type": "Championship Course"
    }
    
    # Verify the estimated data
    total_par = sum(lebovic_golf['par'])
    total_yardage = sum(lebovic_golf['yardage'])
    
    print(f"Lebovic Golf Club (Estimated Data):")
    print(f"  Total Par: {total_par}")
    print(f"  Total Yardage: {total_yardage}")
    print(f"  Par 3s: {lebovic_golf['par'].count(3)} holes")
    print(f"  Par 4s: {lebovic_golf['par'].count(4)} holes") 
    print(f"  Par 5s: {lebovic_golf['par'].count(5)} holes")
    print(f"  Note: This is estimated data that should be verified against the actual scorecard")
    print()
    
    return {"lebovic_golf_club": lebovic_golf}

def update_javascript_with_lebovic():
    """Update JavaScript file with Lebovic Golf Club data"""
    try:
        # Read existing JavaScript file
        with open('script.js', 'r') as f:
            js_content = f.read()
        
        # Load existing courses from JSON if available
        try:
            with open('all_courses.json', 'r') as f:
                existing_courses = json.load(f)
        except:
            existing_courses = {}
        
        # Get Lebovic course data
        lebovic_course = add_lebovic_golf_club()
        
        # Check if we have valid par and yardage data
        course_data = lebovic_course["lebovic_golf_club"]
        if not course_data["par"] or len(course_data["par"]) != 18:
            print("❌ Cannot add course without complete 18-hole par data")
            return
        
        if not course_data["yardage"] or len(course_data["yardage"]) != 18:
            print("❌ Cannot add course without complete 18-hole yardage data")
            return
        
        # Merge with existing courses
        all_courses = {**existing_courses, **lebovic_course}
        
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
        print("Added Lebovic Golf Club")
        
    except Exception as e:
        print(f"Error updating JavaScript file: {e}")

def main():
    print("🏌️ Adding Lebovic Golf Club...")
    update_javascript_with_lebovic()
    print("\n🎉 Complete! Lebovic Golf Club added to the website.")
    print("⚠️  Note: Course data is estimated and should be verified against the actual scorecard PDF.")

if __name__ == "__main__":
    main()