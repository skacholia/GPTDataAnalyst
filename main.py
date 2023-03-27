import pinecone
import streamlit as st
import os.path
import pathlib
from streamlit_chat import message
from langchain.llms import OpenAIChat
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings


st.write("""
# GPT Data Analyst
""")
file = st.file_uploader("Choose a CSV file")

if file is not None:
    df= pd.read_csv(file)
    st.write(df)
