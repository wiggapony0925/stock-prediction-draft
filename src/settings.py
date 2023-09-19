# settings_component.py
import streamlit as st


def settings_sidebar():
    st.sidebar.markdown("## Settings")

    # Text size adjustment
    text_size = st.sidebar.slider("Adjust Text Size", min_value=12, max_value=36, value=16)
    st.markdown(f"<style>body{{font-size:{text_size}px;}}</style>", unsafe_allow_html=True)

    # Theme selection
    theme_options = ["Light", "Dark"]
    selected_theme = st.sidebar.selectbox("Select Theme", theme_options)

    if selected_theme == "Dark":
        st.markdown("<link rel='stylesheet' href='styles.css' class='dark-theme'>", unsafe_allow_html=True)
    else:
        st.markdown("<link rel='stylesheet' href='styles.css' class='light-theme'>", unsafe_allow_html=True)

    # Other settings can be added here
