# main.py
from dotenv import load_dotenv
import os
load_dotenv()

from fetch_bills import get_due_bills
from process_bills import parse_bills
from export import export_to_excel

def main():
    try:
        bills = get_due_bills()
        parsed = parse_bills(bills)
        export_to_excel(parsed)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
