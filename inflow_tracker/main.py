import streamlit as st
import pandas as pd
from dashboard import show_inflows
from fetch_payments import fetch_customer_payments
from fetch_invoices import fetch_expected_invoices
from process import parse_payments, parse_invoices

# Dictionary mapping company names to their org IDs
companies = {
    "ADS Management": "737426804",
    "Thirlmere": "793967859"
}

# Set page title and layout
st.set_page_config(page_title="Multi-Company Inflow Tracker", layout="wide")

st.title("📊 Company-wise Cash Inflow Tracker")

# Create tabs for each company
tabs = st.tabs(list(companies.keys()))

for i, company_name in enumerate(companies.keys()):
    with tabs[i]:
        st.header(f"💼 {company_name}")
        
        # Get current company's org ID
        org_id = companies[company_name]

        try:
            # Fetch and parse actual inflows
            payments_data = fetch_customer_payments(org_id)
            actual = parse_payments(payments_data)

            # Fetch and parse expected inflows
            invoices_data = fetch_expected_invoices(org_id)
            expected = parse_invoices(invoices_data)

            # Show dashboard
            show_inflows(actual, expected)

        except Exception as e:
            st.error(f"❌ Failed to load data for {company_name}: {e}")
