import requests
from datetime import datetime, timedelta
from config import ACCESS_TOKEN, API_DOMAIN

def fetch_customer_payments(org_id):
    today = datetime.today().date()
    past_90 = today - timedelta(days=90)
    future_7 = today + timedelta(days=7)

    url = f"{API_DOMAIN}/books/v3/customerpayments"
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "X-com-zoho-books-organizationid": org_id  # ✅ use the function parameter
    }

    params = {
        "organization_id": org_id,  # ✅ use the function parameter
        "date_start": past_90.isoformat(),
        "date_end": future_7.isoformat()
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("customerpayments", [])
    else:
        raise Exception(f"Customer Payments API Error: {response.text}")
