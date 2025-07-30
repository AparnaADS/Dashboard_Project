import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"
    payload = {
        "refresh_token": os.getenv("ZOHO_REFRESH_TOKEN"),
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "grant_type": "refresh_token"
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception(f"Token refresh failed: {response.text}")
    
    access_token = response.json()["access_token"]
    return access_token


def get_cash_basis_pnl(start_date, end_date):
    access_token = get_access_token()
    org_id = os.getenv("ZOHO_ORGANIZATION_ID")

    url = f"https://www.zohoapis.com/books/v3/reports/profitandloss"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }
    params = {
    "organization_id": org_id,
    "report_basis": "cash",
    "from_date": start_date,
    "to_date": end_date
    }


    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    return response.json()
