from fetch_payments import fetch_customer_payments
from fetch_invoices import fetch_expected_invoices
from process import parse_payments, parse_invoices
from dashboard import show_inflows



def main():
    actual = parse_payments(fetch_customer_payments())
    expected = parse_invoices(fetch_expected_invoices())
    show_inflows(actual, expected)

if __name__ == "__main__":
    import streamlit as st
    st.set_page_config(page_title="Cash Inflow Tracker")
    main()
