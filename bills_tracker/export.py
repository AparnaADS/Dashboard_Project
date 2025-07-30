# streamlit_app.py
import streamlit as st
import pandas as pd
from fetch_bills import get_due_bills
from process_bills import parse_bills

st.set_page_config(page_title="Upcoming Bills", layout="wide")

st.title("📋 Upcoming Due Bills (Next 7 Days)")

try:
    bills = get_due_bills()
    parsed_bills = parse_bills(bills)
    df = pd.DataFrame(parsed_bills)

    if df.empty:
        st.info("✅ No unpaid bills due within the next 7 days.")
    else:
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"❌ Failed to fetch bills: {e}")
