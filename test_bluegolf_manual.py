import requests
from bs4 import BeautifulSoup
import json

def inspect_bluegolf_page():
    """Inspect the BlueGolf page structure to understand the HTML"""
    url = "https://course.bluegolf.com/bluegolf/course/course/humbervalleygc/detailedscorecard.htm"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to fetch page: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Save the HTML for inspection
        with open('humber_valley_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        
        print("✅ Page saved to 'humber_valley_page.html'")
        
        # Extract and analyze structure
        print("\n=== PAGE ANALYSIS ===")
        
        # Look for title
        title = soup.find('title')
        print(f"Title: {title.get_text() if title else 'Not found'}")
        
        # Look for all tables
        tables = soup.find_all('table')
        print(f"\nFound {len(tables)} tables")
        
        for i, table in enumerate(tables):
            rows = table.find_all('tr')
            print(f"  Table {i+1}: {len(rows)} rows")
            
            # Show first few rows to understand structure
            for j, row in enumerate(rows[:3]):
                cells = row.find_all(['td', 'th'])
                cell_texts = [cell.get_text().strip()[:20] for cell in cells]
                print(f"    Row {j+1}: {len(cells)} cells - {cell_texts}")
        
        # Look for specific patterns
        print("\n=== LOOKING FOR SCORECARD DATA ===")
        
        # Search for text containing "par"
        text = soup.get_text().lower()
        if 'par' in text:
            lines = text.split('\n')
            par_lines = [line.strip() for line in lines if 'par' in line.lower() and len(line.strip()) > 5]
            print("Lines containing 'par':")
            for line in par_lines[:5]:  # Show first 5
                print(f"  {line[:100]}")
        
        # Look for numeric patterns that might be scorecard data
        import re
        
        # Look for sequences of 18 numbers (could be par or yardage)
        number_sequences = re.findall(r'(\d+(?:\s+\d+){17})', text)
        if number_sequences:
            print(f"\nFound {len(number_sequences)} sequences of 18 numbers:")
            for i, seq in enumerate(number_sequences):
                numbers = seq.split()
                print(f"  Sequence {i+1}: {numbers}")
        
        # Basic course info extraction
        print(f"\n=== BASIC EXTRACTION ATTEMPT ===")
        
        # Try to extract course name from title
        if title:
            title_text = title.get_text().strip()
            course_name = title_text.replace('Scorecard', '').replace('Golf Course', 'Golf Course').strip()
            print(f"Extracted course name: {course_name}")
        
        print("\nInspection complete! Check 'humber_valley_page.html' for full structure.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_bluegolf_page()