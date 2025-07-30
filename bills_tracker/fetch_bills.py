import requests
from datetime import datetime, timedelta
from config import ORG_ID, ACCESS_TOKEN

def get_due_bills():
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    url = "https://www.zohoapis.com/books/v3/bills"  # 🔥 Hardcoded directly here
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"
    }
    params = {
        "organization_id": ORG_ID,
        "status": "unpaid",
        "due_date_start": today.isoformat(),
        "due_date_end": end_date.isoformat()
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("bills", [])
    else:
        raise Exception(f"API Error: {response.text}")
