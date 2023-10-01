import langchain_helper as lch
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Pet Name Generator")

breed = st.sidebar.selectbox('What is the breed of your dog?', ('chow-chow', 'pug', 'bulldog', 'poodle', 'beagle'))
pet_color = st.sidebar.text_input(label='What is the color of your dog?', max_chars=20)

if pet_color:
    response = lch.generate_pet_name(breed, pet_color)

    st.text(response['pet_names'])