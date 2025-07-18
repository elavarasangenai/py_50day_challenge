import streamlit as st

# Title for the Streamlit app
st.title("Word Reverser - Reverse Each Word in a Sentence")


# Step 1: Get user input for the sentence
with st.form("reverse_form"):
    sentence = st.text_input("Enter a sentence:")
    submitted = st.form_submit_button("Reverse Words")

# Step 2: Function to reverse each word in the sentence
def reverse_individual_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse each word and keep them in a list
    reversed_words = [word[::-1] for word in words]
    # Join the reversed words back into a sentence
    return ' '.join(reversed_words)

# Step 3: Display the reversed sentence when the button is pressed
if submitted and sentence:
    reversed_sentence = reverse_individual_words(sentence)
    st.write(f"Output: {reversed_sentence}")

# Step 4: Few-shot examples for user reference
st.markdown("""
**Few Shots**
- Input: I Love Social Eagle
- Output: I evol laicos elgae
""")
