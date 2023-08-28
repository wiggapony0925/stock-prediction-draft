import streamlit as st
import requests
from volume_stock import find_stocks

def main():
    # Set the page configuration
    st.set_page_config(
        page_title="Stock Prediction Model",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Use Markdown for a more styled title
    st.markdown("# 📈 Stock Prediction Model")
    st.markdown("___")

    # Fetch the most active stocks
    stocks = find_stocks()

    # Check if 'selected_stock' is already in the session state
    if 'selected_stock' not in st.session_state:
        st.session_state.selected_stock = None

    # Create columns for layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Select a Stock")
        # Use selectbox to let the user choose one stock
        st.session_state.selected_stock = st.selectbox("", stocks)

    with col2:
        if st.session_state.selected_stock:
            st.markdown("### Selected Stock")
            st.write(f"🔹 {st.session_state.selected_stock}")

    # Add some space
    st.markdown("---")
    st.markdown("### Additional Features Coming Soon!")
    st.markdown("Stay tuned for more interactive features and insights on your selected stock.")


if __name__ == "__main__":
    main()
