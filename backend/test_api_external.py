import requests

BASE_URL = "http://127.0.0.1:8000/api"

def test_api():
    # 1. Login
    print("Logging in as raja@botola.ma...")
    login_payload = {
        "email": "raja@botola.ma",
        "password": "123456"
    }
    try:
        resp = requests.post(f"{BASE_URL}/auth/login", json=login_payload)
        if resp.status_code != 200:
            print(f"Login failed: {resp.status_code} - {resp.text}")
            return
        
        data = resp.json()
        token = data.get("token")
        print(f"Login success! Token obtained.")
        
        # 2. Fetch Players
        print("Fetching players...")
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(f"{BASE_URL}/players", headers=headers)
        
        if resp.status_code == 200:
            players = resp.json()
            print(f"Success! Found {len(players)} players.")
            if len(players) > 0:
                print(f"First player: {players[0]}")
        else:
            print(f"Fetch failed: {resp.status_code} - {resp.text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
