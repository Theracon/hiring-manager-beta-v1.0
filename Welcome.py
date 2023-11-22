from dotenv import load_dotenv
import streamlit as st


def main():
    load_dotenv()

    st.set_page_config(page_title="Adele AI (beta)",
                       layout="centered", page_icon="🏠")
    st.header("Welcome.")
    st.subheader("Adele AI v1.0 beta")
    st.divider()
    st.divider()
    st.caption("Adele AI (c) 2023. All rights reserved.")


if __name__ == '__main__':
    main()
