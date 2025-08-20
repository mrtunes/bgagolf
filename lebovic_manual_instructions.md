# Adding Lebovic Golf Club - Manual PDF Data Extraction

## PDF Scorecard Location
https://lebovicgolfclub.ca/images/sitepicts/scorecard/02%20Labovic%20Proof%20Mar%2015%202024.pdf

## What You Need to Extract

To accurately add Lebovic Golf Club to the website, please download the PDF and extract:

### 1. Basic Course Information
- Full course name
- Exact location (city, province)
- Total par
- Total yardage

### 2. Hole-by-Hole Data (18 holes)
For each hole (1-18), extract:
- **Par value** (3, 4, or 5)
- **Yardage** (from preferred tee - usually Blue or White)

### 3. Tee Information
- Which tee set to use (Blue, White, Red, etc.)
- Total yardage for that tee set

## Expected Format

Once you have the data, update the `add_lebovic_golf.py` file with:

```python
lebovic_golf = {
    "name": "Lebovic Golf Club",
    "location": "Aurora, ON, Canada",  # Update with exact location
    "par": [4, 3, 5, 4, ...],  # 18 values from the scorecard
    "yardage": [420, 180, 530, 410, ...],  # 18 values from the scorecard
    "tee_info": "Blue Tees",  # Update with actual tee name
    "source": "lebovicgolfclub.ca",
    "url": "https://lebovicgolfclub.ca/images/sitepicts/scorecard/02%20Labovic%20Proof%20Mar%2015%202024.pdf",
    "course_type": "Championship Course"
}
```

## Verification

Make sure:
- ✅ Par array has exactly 18 values
- ✅ Yardage array has exactly 18 values  
- ✅ All par values are 3, 4, or 5
- ✅ All yardage values are reasonable (50-800 yards)
- ✅ Total par adds up correctly
- ✅ Total yardage matches scorecard

## Alternative: Course Website

If the PDF is difficult to read, you can also check:
- Lebovic Golf Club website: https://lebovicgolfclub.ca/
- Look for course information or scorecard pages
- Search for "Lebovic Golf Club scorecard" online

## Current Status

I've created estimated data as a placeholder, but this should be replaced with actual scorecard data for accuracy.