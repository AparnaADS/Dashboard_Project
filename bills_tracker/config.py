import os
from dotenv import load_dotenv
import requests

load_dotenv()

CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ORG_ID = os.getenv("ZOHO_ORG_ID")
API_DOMAIN = "https://www.zohoapis.com"

if not all([CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, ORG_ID]):
    raise ValueError("Missing required environment variables.")

# Generate Access Token
def get_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token"
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Error refreshing token: {response.text}")

# Export for use
ACCESS_TOKEN = get_access_token()
