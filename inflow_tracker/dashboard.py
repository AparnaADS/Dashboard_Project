import streamlit as st
import pandas as pd

def show_inflows(actual, expected):
    combined = actual + expected
    df = pd.DataFrame(combined)


    if "date" not in df.columns:
        st.error("❌ 'date' column is missing. Please check the structure of actual/expected data.")
        return

    # Proceed only if 'date' exists
    df["date"] = pd.to_datetime(df["date"], errors="coerce")  # handle invalid dates as NaT
    df = df.sort_values(by="date")

    st.title("💸 Cash Inflow Tracker")
    st.dataframe(df)

