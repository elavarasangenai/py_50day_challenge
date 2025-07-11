import streamlit as st

def count_numbers(numbers):
    pos = neg = zero = 0
    for n in numbers:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
    return pos, neg, zero

st.title("Count Positive, Negative, and Zero Numbers")

input_str = st.text_area("Enter numbers separated by commas:")

if st.button("Count Numbers"):
    try:
        num_list = [int(x.strip()) for x in input_str.split(',') if x.strip()]
        pos, neg, zero = count_numbers(num_list)
        st.success(f"Positive numbers: {pos}")
        st.info(f"Zero numbers: {zero}")
        st.warning(f"Negative numbers: {neg}")
    except ValueError:
        st.error("Please enter only integers separated by commas.")
