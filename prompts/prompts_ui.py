from langchain_openai import ChatOpenAI

from dotenv import load_dotenv()

import streamlit as st


st.header('Research tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    result = model.invoke(user_prompt)
    st.write(result.content)