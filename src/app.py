import streamlit as st
import requests
from volume_stock import find_stocks


def main():
    st.title("Stock Prediction Model")

    stocks = find_stocks()
    st.multiselect("here are todays stocks", stocks)


if __name__ == "__main__":
    main()
