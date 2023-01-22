import openai
import cv2
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("api_key")

prompt = st.text_input('what do u want','credit score bank')

n=5
response = openai.Image.create(
  prompt=prompt,
  n=5,
  size="512x512"
)

for i in range(n):

    image_url = response['data'][i]['url']

    cap = cv2.VideoCapture(image_url)
    if( cap.isOpened() ) :
        ret,img = cap.read()
        st.image(img)
        cv2.waitKey()