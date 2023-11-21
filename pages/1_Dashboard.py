import streamlit as st
from PyPDF2 import PdfReader

from utils.authenticate import authenticate_user
from utils.transcribe import transcribe_audio
from utils.analyze import analyze_text


if not authenticate_user():
    st.stop()

st.set_page_config(page_title="Dashboard", page_icon="🔓")
st.header("Dashboard")
st.divider()
st.sidebar.success("Welcome to your Dashboard!")

project_name = 'adele-405718'
language_codes = ["en-US", "es-ES"]
user_question = ""
mode = st.radio(
    "**What's your preferred input method?**",
    ["Text :pencil:", "Audio :microphone:"],
    captions=["Enter plain text in English.", "Upload an audio file."]
)

if mode == "Text :pencil:":
    user_question = st.text_area("Enter your question here:")
elif mode == "Audio :microphone:":
    user_question = st.file_uploader("Upload audio file", type="wav")
    file_name = f"{user_question.name}"

if user_question:
    if file_name:
        transcript = transcribe_audio(project_name, file_name, language_codes)
        st.divider()
        st.write("Transcribed Audio:")
        st.write(transcript)
        st.button('Edit')
        st.divider()
    if mode == 'Enter Text':
        user_question = user_question
    else:
        user_question = transcript

# upload context file
context = PdfReader("AdeleAI-v1.0.pdf")
if st.button('Go!', type='primary'):
    analyze_text(context, user_question)
st.divider()
st.caption("Adele AI (c) 2023. All rights reserved.")
