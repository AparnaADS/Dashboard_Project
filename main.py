from api import get_cash_basis_pnl
from utils import get_previous_month_date_range, save_report_to_csv

def main():
    # Step 1: Get previous month's date range
    start_date, end_date = get_previous_month_date_range()
    print(f"📅 Fetching Cash P&L Report from {start_date} to {end_date}...")

    # Step 2: Call the API
    try:
        report_data = get_cash_basis_pnl(start_date, end_date)
        print(report_data)  # 👈 Add this to inspect what’s coming
    except Exception as e:
        print(f"❌ Failed to fetch report: {e}")
        return

    # Step 3: Save to CSV
    save_report_to_csv(report_data)

if __name__ == "__main__":
    main()
