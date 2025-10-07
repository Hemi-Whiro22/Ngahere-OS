# 7. scripts/summon.py
import requests, sys

def summon(manu, action):
    url = f"http://localhost:8000/{manu}/{action}"
    try:
        response = requests.post(url)
        print(f"[{manu.upper()}] {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Failed to summon {manu}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: summon.py [manu] [action]")
    else:
        summon(sys.argv[1], sys.argv[2])
