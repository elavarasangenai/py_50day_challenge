import streamlit as st

# Title of the app
st.title("Name Formatter")

# Description
st.write("Enter your full name to see it in different formats.")

# Input box for full name
full_name = st.text_input("Enter your full name:", "")

# Button to format name
if st.button("Format Name"):
    # Step 1: Split the name into parts
    name_parts = full_name.strip().split()
    
    # Step 2: Extract first and last name
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
    elif len(name_parts) == 1:
        first_name = name_parts[0]
        last_name = ""
    else:
        first_name = ""
        last_name = ""
    
    # Step 3: Display different formats
    st.write(f"First Name: {first_name}")
    st.write(f"Last Name: {last_name}")
    st.write(f"Upper Case: {full_name.upper()}")
    st.write(f"Lower Case: {full_name.lower()}")
    # Camel Case: Each word capitalized
    camel_case = ' '.join([word.capitalize() for word in name_parts])
    st.write(f"Camel Case: {camel_case}")
    # Last, First format
    if first_name and last_name:
        st.write(f"Last, First: {last_name}, {first_name}")
    
# Example usage
st.info("Example: Social Eagle → First Name: Social, Last Name: Eagle, Upper Case: SOCIAL EAGLE, Lower Case: social eagle, Camel Case: Social Eagle, Last, First: Eagle, Social")
