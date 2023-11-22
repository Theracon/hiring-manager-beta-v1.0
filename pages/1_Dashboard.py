import streamlit as st
from PyPDF2 import PdfReader

from utils.authenticate import authenticate_user
from utils.transcribe import transcribe_audio
from utils.analyze import analyze_text
from utils.sanitize import sanitize_bytes


if not authenticate_user():
    st.stop()

st.set_page_config(page_title="Dashboard", page_icon="🔓")
st.header("Dashboard")
st.divider()
st.sidebar.success("Welcome to your Dashboard!")

# upload context file
context = PdfReader("AdeleAI-v1.0.pdf")

project_name = 'adele-405718'
language_codes = ["en-US", "es-ES"]
mode = st.radio(
    "**What's your preferred input method?**",
    ["Text :pencil:", "Audio :microphone:"],
    captions=["Enter plain text in English.", "Upload an audio file."]
)

if mode == "Text :pencil:":
    text_manuscript = st.text_area("Enter your question here:")
    if text_manuscript:
        audio_manuscript = None
        st.divider()
        if st.button('Go!', type='primary'):
            analyze_text(context, text_manuscript)
else:
    text_manuscript = None
    audio_manuscript = st.file_uploader("Upload audio file", type="wav")
    if audio_manuscript is not None:
        raw_bytes = audio_manuscript.getvalue()
        sanitized_bytes = sanitize_bytes(raw_bytes)
        if sanitized_bytes:
            transcript = transcribe_audio(
                project_name, raw_bytes, language_codes)
            st.divider()
            st.write("Audio Transcript:")
            st.write(transcript)
            st.button('Edit')
            st.divider()
            if st.button('Go!', type='primary'):
                analyze_text(context, transcript)
st.divider()
st.caption("Adele AI (c) 2023. All rights reserved.")
