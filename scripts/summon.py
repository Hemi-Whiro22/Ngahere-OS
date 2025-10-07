# summon.py
import requests
import sys

def summon(manu_name, action):
    endpoint = f"http://localhost:8000/{manu_name}/{action}"
    response = requests.post(endpoint)
    if response.ok:
        print(f"[{manu_name.upper()}] Responded:\n{response.text}")
    else:
        print(f"Failed to summon {manu_name}: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python summon.py [manu_name] [action]")
        sys.exit(1)
    summon(sys.argv[1], sys.argv[2])
