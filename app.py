import streamlit as st
from src.routing import run_prediction_page, run_insights_page

# 1. Page Configuration
st.set_page_config(
    page_title="Arabic Customer Intelligence",
    page_icon="📊",
    layout="wide"
)

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page:", ["💬 Single Review Prediction", "📈 Company Insights"])

# 3. Route to Respective Page
if page == "💬 Single Review Prediction":
    run_prediction_page()
elif page == "📈 Company Insights":
    run_insights_page()