import openai
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("api_key")


st.title("I am here to HELP, please go ahead")
model_engine = "text-davinci-003"
prompt = st.text_input('Ask ur Question','credit score kya hota hai ')

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
st.write(response)