import requests

URL = 'https://jsonplaceholder.typicode.com/users'

try:
    r = requests.get(URL)
except:
    print("Network or HTTP error")
    exit(1)

if r.status_code!=200:
    print("Failed to fetch data")
    print("Error Code:",r.status_code)

try:
    data = r.json()
except:
    print("Response did not contain valid JSON")
    exit(1)
    
n = len(data)

for i in range(n):
    user = data[i]
    if user["address"]["city"].lower().startswith("s"):
        print(f"User {i}:")
        print(" Name:",user["name"])
        print(" Username:",user["username"])
        print(" Email:",user["email"])
        print(" City:",user["address"]["city"])