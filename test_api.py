import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOLF_API_KEY')
base_url = "https://api.golfcourseapi.com"

# Test different authentication methods
auth_methods = [
    {'X-API-Key': api_key},
    {'Authorization': f'Bearer {api_key}'},
    {'Authorization': f'Token {api_key}'},
    {'apikey': api_key}
]

endpoints = [
    f"{base_url}/courses",
    f"{base_url}/golf-courses", 
    f"{base_url}/api/courses",
    f"{base_url}/api/golf-courses",
    f"{base_url}/v1/courses",
    f"{base_url}/v1/golf-courses"
]

print(f"Testing API with key: {api_key[:10]}...")

for auth in auth_methods:
    print(f"\n--- Testing auth method: {list(auth.keys())[0]} ---")
    
    for endpoint in endpoints:
        try:
            response = requests.get(endpoint, headers=auth, timeout=10)
            print(f"{endpoint}: {response.status_code}")
            
            if response.status_code == 200:
                print(f"SUCCESS! Response: {response.text[:200]}")
                break
            elif response.status_code != 404:
                print(f"Error response: {response.text[:100]}")
                
        except Exception as e:
            print(f"{endpoint}: Exception - {e}")
    
    # If we found a working endpoint, stop testing
    if response.status_code == 200:
        break