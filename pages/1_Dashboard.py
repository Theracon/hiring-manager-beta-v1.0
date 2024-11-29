import streamlit as st
from PyPDF2 import PdfReader

from utils.authenticate import authenticate_user
from utils.transcribe import transcribe_audio
from utils.analyze import analyze_text
# from utils.sanitize import sanitize_bytes


if not authenticate_user():
    st.stop()

st.set_page_config(page_title="Dashboard", page_icon="🔓")
st.header("Your Dashboard")
st.divider()
st.sidebar.success("Welcome to your Dashboard!")

# upload context file
transcript_edit = False
transcript_edit_btn_text = 'Edit'
st.session_state["transcript_edit"] = False
st.session_state["transcript_edit_btn_text"] = 'Edit'
st.session_state["submit_btn_disabled"] = True

st.subheader("How It Works (2 easy steps):")
st.write("1. Upload your document (this could be a textbook, handout, or note.)")
st.write("2. Ask a question (you can either write your question or upload an audio file.)")
st.write("")

context = None
uploaded_file = None
try:
    uploaded_file = st.file_uploader(
        label="Upload your textbook, handout, or note here (PDF only)", key=1)
    if uploaded_file is not None:
        st.success("File uploaded!")
        context = PdfReader(uploaded_file)
        st.session_state["submit_btn_disabled"] = False
except FileNotFoundError as e:
    st.error(f"File not found. {e}")
except Exception as e:
    st.error(f"Something went wrong. Please try again. {e}")


project_name = 'adele-405718'
language_codes = ["en-US"]
result = None

if context is not None:
    st.text("")
    st.divider()
    st.subheader("Ask your questions, one at a time 😊:")
    mode = st.radio(
        "**How do you want to ask your question?**",
        ["Write it :pencil:", "Import an audio file :microphone:"],
        captions=["Enter plain text in English.", "Upload an audio file."]
    )

    if mode == "Write it :pencil:":
        text_manuscript = st.text_input("Enter your question here:")
        if text_manuscript:
            audio_manuscript = None
            if st.button('Send', type='primary', disabled=st.session_state["submit_btn_disabled"]):
                analyze_text(context, text_manuscript)

    else:
        text_manuscript = None
        audio_manuscript = st.file_uploader("Upload audio file", type="wav")
        if audio_manuscript is not None:
            raw_bytes = audio_manuscript.getvalue()
            # sanitized_bytes = sanitize_bytes(raw_bytes)
            if raw_bytes:
                transcript = transcribe_audio(
                    project_name, raw_bytes, language_codes)
                st.divider()
                st.write("Audio Transcript:")
                st.write(transcript)
                if st.session_state["transcript_edit"]:
                    new_text = st.text_area(
                        "Enter your question here:", value=transcript)
                if st.button(st.session_state["transcript_edit_btn_text"]):
                    if st.session_state["transcript_edit"]:
                        st.session_state["transcript_edit"] = False
                        st.session_state["transcript_edit_btn_text"] = 'Edit'
                    else:
                        st.session_state["transcript_edit"] = True
                        st.session_state["transcript_edit_btn_text"] = 'Done'
                st.divider()
                if st.button('Magic!', type='primary'):
                    analyze_text(context, transcript)

st.divider()
st.caption("Notoris Technologies (c) 2024. All rights reserved.")
