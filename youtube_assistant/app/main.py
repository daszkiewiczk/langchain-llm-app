import langchain_helper as lch
import streamlit as st
from dotenv import load_dotenv
import textwrap

load_dotenv()

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label='Enter a Youtube URL',
            max_chars=100,
        )
        query = st.sidebar.text_area(
            label='Ask a question about the video',
            max_chars=100,
        )

        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.text('Answer:')
    st.text(textwrap.fill(response, width=80))
    st.subheader("Video Transcript")
    st.text(textwrap.fill(docs, width=80))
    