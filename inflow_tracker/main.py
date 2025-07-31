import streamlit as st
from fetch_payments import fetch_customer_payments
from fetch_invoices import fetch_expected_invoices
from process import parse_payments, parse_invoices
from dashboard import show_inflows

def main():
    st.set_page_config(page_title="Cash Inflow Tracker")

    # Step 1: Get raw data
    raw_actual = fetch_customer_payments()
    raw_expected = fetch_expected_invoices()

    # Step 2: Parse it
    actual = parse_payments(raw_actual)
    expected = parse_invoices(raw_expected)

    # Step 4: Check if data exists
    if not actual and not expected:
        st.error("❌ 'date' column is missing. No data was returned from Zoho APIs.")
        return

    # Step 5: Show dashboard
    show_inflows(actual, expected)

if __name__ == "__main__":
    main()
