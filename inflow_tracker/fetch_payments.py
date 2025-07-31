import requests
from datetime import datetime, timedelta
from config import ACCESS_TOKEN, ORG_ID, API_DOMAIN

def fetch_customer_payments():
    today = datetime.today().date()
    past_30 = today - timedelta(days=30)
    future_7 = today + timedelta(days=7)

    url = f"{API_DOMAIN}/books/v3/customerpayments"
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"
    }
    params = {
        "organization_id": ORG_ID,
        "date_start": past_30.isoformat(),
        "date_end": future_7.isoformat()
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("customerpayments", [])
    else:
        raise Exception(f"Customer Payments API Error: {response.text}")
