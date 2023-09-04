import streamlit as st
import plotly.graph_objects as go
from volume_stock import find_stocks
from stockInformation import stock_information
from dataframe import fetch_stock_data, display_stock_data, date_range
import config


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
        selected_stock = st.selectbox("Select a stock", stocks, index=stocks.index(
            st.session_state.selected_stock) if st.session_state.selected_stock else 0)
        confirm_button = st.button("Confirm Stock")
        st.session_state.selected_stock = selected_stock if confirm_button else st.session_state.selected_stock
        config.selected_stock = st.session_state.selected_stock

        # Add a "Learn More" link
        st.markdown("[ℹ️ Learn more about stock selection](#)")

    with col2:
        if st.session_state.selected_stock:
            st.markdown("### Selected Stock")
            st.write(f"🔹 {st.session_state.selected_stock}")
        else:
            st.markdown("### No Stock Selected")

    st.markdown("---")
    st.markdown("## Stock Description")

    stock_info = stock_information()
    if st.session_state.selected_stock and stock_info is not None:
        with st.spinner("Fetching stock information..."):
            company_name = stock_info.get("Company Name", "N/A")
            industry = stock_info.get("Industry", "N/A")
            website = stock_info.get("Website", "N/A")
            description = stock_info.get("Description", "N/A")

            st.write(f"**Company Name:** {company_name}")
            st.write(f"**Industry:** {industry}")
            st.write(f"**Website:** [{website}]({website})")
            st.write(f"**Description:** {description}")
    elif st.session_state.selected_stock:
        st.error("Stock information not available.")

    # Add a separator
    st.markdown("---")

    # Add a date range picker with a default range
    selected_start_date, selected_end_date = date_range()
    st.markdown("### Date Range")
    with st.expander("Select a Date Range"):
        selected_start_date = st.date_input("Start Date", selected_start_date)
        selected_end_date = st.date_input("End Date", selected_end_date)

    if st.session_state.selected_stock is not None:
        stock_data = fetch_stock_data(st.session_state.selected_stock, selected_start_date, selected_end_date)

        if stock_data is not None:
            st.markdown("## Stock Price Chart")
            fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                                 open=stock_data['Open'],
                                                 high=stock_data['High'],
                                                 low=stock_data['Low'],
                                                 close=stock_data['Close'])])
            st.plotly_chart(fig)

            # Display stock data using the display_stock_data function
            display_stock_data(st.session_state.selected_stock, selected_start_date, selected_end_date)
        else:
            st.warning("Stock data not available.")
    else:
        st.warning("Please select a stock before fetching and displaying stock data.")

    # Add a separator
    st.markdown("---")

    # Add a button to show a popup with additional features
    if st.button("🚀 Explore Additional Features"):
        st.write("Stay tuned for more interactive features and insights on your selected stock.")
        # Add more content or features in the future

    # Add a footer with a "Feedback" link
    st.markdown("<div style='text-align: center; margin-top: 20px;'>"
                "<a href='#' style='color: #888;'>Provide Feedback</a></div>",
                unsafe_allow_html=True)


if __name__ == "__main__":
    main()

