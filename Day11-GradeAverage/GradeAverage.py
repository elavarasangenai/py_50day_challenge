
# GradeAverage.py
# Streamlit app to calculate average of 5 test scores and determine pass/fail
# Each subject is checked for pass/fail (pass mark is 35)
# Displays total, average, and overall result

import streamlit as st

# Step 1: Define subjects
subjects = ['Tamil', 'English', 'Maths', 'Science', 'Social']
scores = []

st.title("Grade Average Calculator")
st.write("Enter the scores for each subject (0-100):")

# Step 2: Get input for each subject using Streamlit number_input
for subject in subjects:
    score = st.number_input(f"{subject} score", min_value=0, max_value=100, value=0, step=1)
    scores.append(score)

# Step 3: Check pass/fail for each subject
pass_mark = 35
results = []
for i, score in enumerate(scores):
    status = "Pass" if score >= pass_mark else "Fail"
    results.append(f"{subjects[i]} - {score} ({status})")

# Step 4: Calculate total and average
total = sum(scores)
average = total / len(scores)

# Step 5: Determine overall result
overall_result = "Pass" if all(score >= pass_mark for score in scores) else "Fail"

# Step 6: Display results using Streamlit
st.subheader("Subject Results:")
st.write(", ".join(results))
st.write(f"**Total :** {total}")
st.write(f"**Average :** {average:.0f} %")
st.write(f"**Result :** {overall_result}")
