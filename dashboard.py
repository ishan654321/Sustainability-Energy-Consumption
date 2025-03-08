import streamlit as st
def dashcontent():
    st.subheader('Renewable Energy Production Dashboard')
    st.markdown("""
        <iframe title="Renewable Energy Dashboard" width="800" height="450" src="https://app.powerbi.com/view?r=eyJrIjoiOTgzNjA3YjQtNmM2Mi00NGNiLWE4MWItODhlZGUxNTc2ZTg0IiwidCI6IjExMTNiZTM0LWFlZDEtNGQwMC1hYjRiLWNkZDAyNTEwYmU5MSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>
        """, unsafe_allow_html=True)
