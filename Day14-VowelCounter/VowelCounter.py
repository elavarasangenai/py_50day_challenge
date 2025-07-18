import streamlit as st

# Title of the app
st.title("Vowel Counter")

# Description
st.write("Enter a word or sentence to count the number of vowels.")

# Input box for the word or sentence
input_text = st.text_input("Enter a word or sentence:", "")

# Button to count vowels
if st.button("Count Vowels"):
    # Step 1: Define vowels
    vowels = "aeiouAEIOU"
    
    # Step 2: Count vowels in the input text
    count = 0
    for char in input_text:
        if char in vowels:
            count += 1
    
    # Step 3: Display the result
    st.success(f"Total vowel is {count}.")

# Example usage
st.info("Example: Social Eagle → Output: total vowel is 6.")
