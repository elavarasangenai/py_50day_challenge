import streamlit as st

st.title("Simple Password Validator")

password = st.text_input("Enter your password", type="password")
if st.button("Submit"):
    if len(password) < 8:
        st.error("Password is Invalid")
    else:
        st.success(f"password length is : {len(password)}")
