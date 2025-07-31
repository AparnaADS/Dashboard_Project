import requests
from datetime import datetime
from config import ACCESS_TOKEN, ORG_ID, API_DOMAIN

def fetch_expected_invoices():
    today = datetime.today().date()

    url = f"{API_DOMAIN}/books/v3/invoices"
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"
    }
    params = {
        "organization_id": ORG_ID,
        "status": "draft",
        "due_date_start": today.isoformat()
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("invoices", [])
    else:
        raise Exception(f"Invoices API Error: {response.text}")
