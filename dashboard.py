import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cash P&L Dashboard", layout="wide")

st.title("📊 Profit & Loss Report (Cash Basis)")
st.caption("Previous Month Report")

# Load CSV
df = pd.read_csv("cash_pnl.csv")

if df.empty:
    st.warning("The report is empty.")
else:
    # Display table
    st.dataframe(df)

    # Summary
    st.subheader("💰 Total Summary")
    total = df.groupby("Category")["Amount (AED)"].sum().reset_index()
    st.bar_chart(total.set_index("Category"))

    # Optional: filter view
    category = st.selectbox("Filter by Category", df["Category"].unique())
    st.dataframe(df[df["Category"] == category])
