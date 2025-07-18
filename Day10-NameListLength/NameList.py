# NameList.py
# Task 1: Store 5 names in a list and print them with their lengths
names = ["Elaa", "Thendral", "Manju", "Rajan", "Karthi"]
print("Task 1: Names and their lengths:")
for name in names:
    print(f"Name is {name} and length is {len(name)}.")

# Task 2: Get 5 user inputs using Streamlit and print the name and length
import streamlit as st

st.title("Name List Length Finder")
st.write("Enter 5 names below:")

user_names = []
for i in range(5):
    user_name = st.text_input(f"Enter name {i+1}", key=f"name_{i}")
    user_names.append(user_name)

if all(user_names):
    st.write("Names and their length:")
    for name in user_names:
        st.write(f"Name is {name} and length is {len(name)}.")
else:
    st.info("Please enter all 5 names to see the results.")
