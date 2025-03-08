import streamlit as st
from dashboard import dashcontent
from tsacode import forcasting
from home import home
from analysis import analysis
from renewable import RenewableEnergy
from ai import ai_viz
from references import ref

# Sidebar with navigation buttons
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home","Dashboards", "Analysis", "Renewable Energy","Forcasting","AI-Crypto-DataCenter Energy Usage","References"))

# Main content based on the selected page
if page == "Home":
    # st.title("Home")
    # st.write("This is the Home section.")
    home()

elif page == "Dashboards":
    # st.title("Dashboards")
    # st.write("This is the Dashboards section.")
    dashcontent()

elif page == "Analysis":
    # st.title("Analysis")
    # st.write("This is the Analysis section.")
    analysis()

elif page == "Renewable Energy":
    # st.title("Renewable Energy")
    # st.write("This is the Renewable Energy section.")
    RenewableEnergy()

elif page=="Forcasting":
    st.title("Time Series Forcasting")
    # st.write("This is the time series analysis section.")
    forcasting()

elif page=="AI-Crypto-DataCenter Energy Usage":
    st.title("AI-Crypto-DataCenter Energy Usage")
    # st.write("This is the AI-Crypto-DataCenter Energy Usage section.")
    ai_viz()

elif page=="References":
    # st.title("AI-Crypto-DataCenter Energy Usage")
    ref()