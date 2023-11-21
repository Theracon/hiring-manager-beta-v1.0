import hmac
import streamlit as st


def authenticate_user():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "PIN", type="password", on_change=password_entered, key="password"
    )
    st.caption('Contact the site administrator for your PIN.')
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False
