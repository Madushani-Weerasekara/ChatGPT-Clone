import os
import streamlit as st # To create webapplication
from langchain_openai import OpenAI # To use OpenAI API
from dotenv import load_dotenv # To load the virtual environment
load_dotenv()

st.title("ChatGPT-Clone")

#set openai api key from stremlit secrets
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo" #We've set a default

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
