import streamlit as st
import pandas as pd

def show_inflows(actual, expected):
    combined = actual + expected
    df = pd.DataFrame(combined)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(by="date")

    st.title("💸 Cash Inflow Tracker")
    st.dataframe(df)
