from dotenv import load_dotenv
import streamlit as st


def main():
    load_dotenv()

    st.set_page_config(page_title="Adele AI (beta)",
                       layout="centered", page_icon="🏠")
    st.header("Welcome to ADELE AI (beta)")
    st.divider()


if __name__ == '__main__':
    main()
