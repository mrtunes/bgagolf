import requests
from bs4 import BeautifulSoup
import json

def inspect_course_page(course_id):
    """Inspect a specific BlueGolf course page"""
    url = f"https://course.bluegolf.com/bluegolf/course/course/{course_id}/detailedscorecard.htm"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"\n📍 Inspecting: {course_id}")
        print(f"URL: {url}")
        
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ Failed to fetch page")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.find('title')
        print(f"Title: {title.get_text() if title else 'Not found'}")
        
        # Look for tables
        tables = soup.find_all('table')
        print(f"Found {len(tables)} tables")
        
        if len(tables) > 0:
            print("\n=== TABLE ANALYSIS ===")
            for i, table in enumerate(tables):
                rows = table.find_all('tr')
                print(f"\nTable {i+1}: {len(rows)} rows")
                
                # Show first few rows
                for j, row in enumerate(rows[:4]):
                    cells = row.find_all(['td', 'th'])
                    cell_texts = [cell.get_text().strip()[:15] for cell in cells]
                    print(f"  Row {j+1}: {len(cells)} cells - {cell_texts}")
        
        # Look for any scorecard-related content
        text = soup.get_text().lower()
        if 'par' in text:
            print(f"\n✅ Found 'par' in page content")
            # Look for numeric sequences
            import re
            sequences = re.findall(r'(\d+(?:\s+\d+){10,})', text)
            if sequences:
                print(f"Found {len(sequences)} number sequences:")
                for seq in sequences[:3]:  # Show first 3
                    numbers = seq.split()
                    print(f"  {numbers}")
        else:
            print(f"\n❌ No 'par' found in page content")
        
        # Save page for manual inspection
        filename = f"{course_id}_page.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print(f"\n💾 Saved page to {filename}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def inspect_all_toronto_courses():
    """Inspect all three Toronto courses"""
    course_ids = [
        'ospreyvalleytoot',
        'scarlettwoodsgc', 
        'donvalleygc'
    ]
    
    print("🔍 Inspecting Toronto golf course pages...")
    
    for course_id in course_ids:
        inspect_course_page(course_id)
        print("\n" + "="*60)

if __name__ == "__main__":
    inspect_all_toronto_courses()