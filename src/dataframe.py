import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
from config import DEFAULT_START_DATE, DEFAULT_END_DATE, selected_stock

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

def display_stock_data(selected_stock, selected_start_date, selected_end_date):
    stock_data = fetch_stock_data(selected_stock, selected_start_date, selected_end_date)

    if stock_data is None:
        return


    chart_options = ["Candlestick Chart", "Line Chart", "OHLC Chart"]
    selected_charts = st.multiselect("Select Charts to Display", chart_options, default=["Candlestick Chart"])

    st.write(f"**Company Name:** {selected_stock}")

    if "Candlestick Chart" in selected_charts:
        fig_candlestick = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                                          open=stock_data['Open'],
                                                          high=stock_data['High'],
                                                          low=stock_data['Low'],
                                                          close=stock_data['Close'])])
        st.plotly_chart(fig_candlestick, use_container_width=True)

    if "Line Chart" in selected_charts:
        st.write(stock_data)  # Display data frame
        fig_line = go.Figure(data=go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines'))
        st.plotly_chart(fig_line, use_container_width=True)

    if "OHLC Chart" in selected_charts:
        fig_ohlc = go.Figure(data=[go.Ohlc(x=stock_data.index,
                                           open=stock_data['Open'],
                                           high=stock_data['High'],
                                           low=stock_data['Low'],
                                           close=stock_data['Close'])])
        st.plotly_chart(fig_ohlc, use_container_width=True)

    st.markdown("Displaying data for selected date range:")
    st.write(f"**Start Date:** {stock_data.index[0]}")
    st.write(f"**End Date:** {stock_data.index[-1]}")

    return stock_data

