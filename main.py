import streamlit as st
import os.path
import pathlib
import pandas as pd

st.write("""
# GPT Data Analyst
""")
file = st.file_uploader("Choose a CSV file")

if file is not None:
    df= pd.read_csv(file)
    st.write(df)
