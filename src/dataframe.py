import yfinance as yf
import streamlit as st
from datetime import datetime, timedelta
from config import selected_stock, DEFAULT_START_DATE, DEFAULT_END_DATE


def date_range():
    st.markdown("## Please choose a range of dates for the data frame")

    selected_start_date = st.date_input("Select start date", DEFAULT_START_DATE)
    selected_end_date = st.date_input("Select end date", DEFAULT_END_DATE)

    return selected_start_date, selected_end_date


def fetch_stock_data(selected_stock, start_date, end_date):
    if start_date is None or end_date is None:
        st.warning("Please select both start and end dates.")
        return None

    if start_date > end_date:
        st.warning("Start date cannot be after end date.")
        return None

    ticker = yf.Ticker(selected_stock)
    stock_data = ticker.history(start=start_date, end=end_date)

    if stock_data.empty:
        st.warning("No data available for the selected date range.")
        return None

    return stock_data


def display_stock_data(stock_data):
    if stock_data is None:
        return

    st.markdown("## Stock Data")

    st.write("Displaying data for selected date range:")
    st.write(f"Start Date: {stock_data.index[0]}")
    st.write(f"End Date: {stock_data.index[-1]}")

    st.line_chart(stock_data["Close"], use_container_width=True)
