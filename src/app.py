import streamlit as st
import config
from volume_stock import find_stocks
from stockInformation import stock_information

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
        config.selected_stock = st.session_state.selected_stock

    with col2:
        if st.session_state.selected_stock:
            st.markdown("### Selected Stock")
            st.write(f"🔹 {st.session_state.selected_stock}")
        else:
            st.markdown("### No Stock Selected")

    st.markdown("---")
    st.markdown(f"## {selected_stock}  Description")

    stock_info = stock_information()
    if st.session_state.selected_stock and isinstance(stock_info, dict):
        with st.spinner("Fetching stock information..."):
            company_name, industry, website, description = stock_info.values()

            st.write(f"**Company Name:** {company_name}")
            st.write(f"**Industry:** {industry}")
            st.write(f"**Website:** [{website}]({website})")
            st.write(f"**Description:** {description}")
    elif st.session_state.selected_stock:
        st.markdown("Stock information not available.")

    st.markdown("### Additional Features Coming Soon!")
    st.markdown("Stay tuned for more interactive features and insights on your selected stock.")



if __name__ == "__main__":
    main()
