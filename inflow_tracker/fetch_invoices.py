import requests
from datetime import datetime
from config import API_DOMAIN, ACCESS_TOKEN

def fetch_expected_invoices(org_id):
    headers = {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "X-com-zoho-books-organizationid": org_id  # ✅ This is required!
    }

    today = datetime.today().strftime('%Y-%m-%d')
    invoices = []
    page = 1

    while True:
        url = f"{API_DOMAIN}/books/v3/invoices?organization_id={org_id}&due_date_start={today}&page={page}"
        response = requests.get(url, headers=headers)
        data = response.json()

        if "invoices" not in data:
            raise Exception(f"Invoices API Error: {response.text}")

        invoices.extend(data["invoices"])

        if not data.get("page_context", {}).get("has_more_page"):
            break

        page += 1

    return invoices
