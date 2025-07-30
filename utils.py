from datetime import date, timedelta
import csv

def get_previous_month_date_range():
    today = date.today().replace(day=1)
    last_day = today - timedelta(days=1)
    start_date = last_day.replace(day=1)
    return start_date.isoformat(), last_day.isoformat()


def save_report_to_csv(data, filename="cash_pnl.csv"):
    try:
        rows = data.get("profit_and_loss", [])
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Subcategory", "Account", "Amount (AED)"])

            for section in rows:
                category_name = section.get("name", "")
                for sub in section.get("account_transactions", []):
                    subcategory = sub.get("name", "")
                    for account in sub.get("account_transactions", []):
                        account_name = account.get("name", "")
                        amount = account.get("total", 0.0)
                        writer.writerow([category_name, subcategory, account_name, amount])

        print(f"✅ Report saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")

