import streamlit as st

# Title of the app
st.title("Find the Largest Number in a List")

# Description
st.write("Enter numbers separated by commas and click 'Check Max' to find the largest number (without using max()).")

# Input box for numbers
numbers_input = st.text_input("Enter numbers separated by commas:", "")

# Button to check maximum
if st.button("Check Max"):
    # Step 1: Split the input string by comma and strip spaces
    numbers_str_list = [num.strip() for num in numbers_input.split(",") if num.strip()]
    
    # Step 2: Convert string list to integer list
    try:
        numbers = [int(num) for num in numbers_str_list]
        
        # Step 3: Find the largest number without using max()
        if numbers:
            largest = numbers[0]  # Assume first number is largest
            for num in numbers:
                if num > largest:
                    largest = num
            # Step 4: Display the result
            st.success(f"Max number is : {largest}")
        else:
            st.warning("Please enter at least one number.")
    except ValueError:
        st.error("Invalid input! Please enter only numbers separated by commas.")

# Example usage
st.info("Example: 2,5,6,6,10 → Output: Max number is : 10")
