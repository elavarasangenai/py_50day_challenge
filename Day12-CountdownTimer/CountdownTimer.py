import streamlit as st
import time

st.title("Countdown Timer")
st.write("This app counts down from 10 to 0.")

# Initialize countdown value in session state
if 'countdown' not in st.session_state:
    st.session_state.countdown = None

start = st.button("Start Countdown")

if start:
    st.session_state.countdown = 10
    st.session_state.running = True
    st.rerun()

if st.session_state.countdown is not None and st.session_state.get('running', False):
    for i in range(st.session_state.countdown, -1, -1):
        st.write(f"Countdown: {i}")
        time.sleep(1)
        st.session_state.countdown = i - 1
        st.rerun()
    st.session_state.running = False
