import streamlit as st
from volume_stock import find_stocks
from stockInformation import stock_information
from dataframe import fetch_stock_data, display_stock_data, date_range

def main():
    st.set_page_config(
        page_title="Stock Prediction Model",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown("# 📈 Stock Prediction Model")
    st.markdown("___")

    stocks = find_stocks()

    if 'selected_stock' not in st.session_state:
        st.session_state.selected_stock = None

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Select a Stock")
        selected_stock = st.selectbox("Select a stock", stocks, index=stocks.index(st.session_state.selected_stock) if st.session_state.selected_stock else 0)
        confirm_button = st.button("Confirm Stock")
        st.session_state.selected_stock = selected_stock if confirm_button else st.session_state.selected_stock

    with col2:
        if st.session_state.selected_stock:
            st.markdown("### Selected Stock")
            st.write(f"🔹 {st.session_state.selected_stock}")
        else:
            st.markdown("### No Stock Selected")

    st.markdown("---")

    selected_start_date, selected_end_date = date_range()

    # Fetch stock data based on selected date range
    stock_data = fetch_stock_data(st.session_state.selected_stock, selected_start_date, selected_end_date)

    # Display stock data using the display_stock_data function
    display_stock_data(stock_data)

    st.markdown("### Additional Features Coming Soon!")
    st.markdown("Stay tuned for more interactive features and insights on your selected stock.")


if __name__ == "__main__":
    main()
