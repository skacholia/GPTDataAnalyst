import streamlit as st
import os
import pathlib
import pandas as pd
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["openai"]

st.write("""
# GPT Data Analyst
""")
file = st.file_uploader("Choose a CSV file")

if file is not None:
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=True, max_iterations = 4)
    q = st.text_input('Ask a question', 'Describe the dataset')
    st.write(agent.run(q + "Include numbers and interpret the data."))
