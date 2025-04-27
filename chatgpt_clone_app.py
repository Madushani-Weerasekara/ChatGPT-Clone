import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

load_dotenv()

st.title("ChatGPT-Clone (Lightweight)")

pipe = pipeline(
    "text2text-generation",             # <-- Important: text2text for FLAN models
    model="google/flan-t5-small",        # <-- Small free model
    max_length=256,
    do_sample=True,
    temperature=0.7
)

client = HuggingFacePipeline(pipeline=pipe)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
