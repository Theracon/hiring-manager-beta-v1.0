from dotenv import load_dotenv
import streamlit as st


def main():
    load_dotenv()

    st.set_page_config(page_title="AI QA (BETA)",
                       layout="centered", page_icon="📔")
    st.header("AI Q&A (v1.0.0)")
    st.warning("BETA")
    st.subheader("Say Hello 👋🏽 to your new to your study companion!")
    st.divider()
    st.write("Click on Dashboard in the sidebar to get started!")
    st.divider()
    st.caption("Notoris Technologies (c) 2024. All rights reserved.")


if __name__ == '__main__':
    main()
