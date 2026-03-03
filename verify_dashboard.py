import os
import django
from django.test import Client

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_analyst_project.settings')
django.setup()

def verify():
    client = Client()
    
    # 1. Test GET request
    print("Testing GET / ...")
    response = client.get('/')
    if response.status_code == 200:
        print("SUCCESS: Dashboard loaded correctly.")
        if "Autonomous CSV Analyst" in response.content.decode():
            print("SUCCESS: Header found.")
    else:
        print(f"FAILED: Dashboard returned status {response.status_code}")
        return

    # 2. Test POST request (Query)
    print("\nTesting POST / with query 'What is the total sales?' ...")
    response = client.post('/', {'query': 'What is the total sales?'})
    if response.status_code == 200:
        content = response.content.decode()
        if "584" in content:
            print("SUCCESS: Agent returned correct result (584).")
        else:
            print(f"FAILED: Agent result not found in response. Content length: {len(content)}")
    else:
        print(f"FAILED: POST request returned status {response.status_code}")

    # 3. Test Plot request
    print("\nTesting POST / with query 'Plot sales over time' ...")
    response = client.post('/', {'query': 'Plot sales over time'})
    if response.status_code == 200:
        content = response.content.decode()
        if "sales_over_time.png" in content:
            print("SUCCESS: Chart URL found in response.")
            media_path = os.path.join('media', 'sales_over_time.png')
            if os.path.exists(media_path):
                print(f"SUCCESS: Chart file exists at {media_path}")
        else:
            print("FAILED: Chart URL not found in response.")
    else:
        print(f"FAILED: Plot request returned status {response.status_code}")

if __name__ == "__main__":
    verify()
