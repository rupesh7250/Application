import streamlit as st

# Page Configuration
st.set_page_config(page_title="Student Result App", page_icon="🎓", layout="centered")

st.title("🎓 Student Result Management System")

st.write("Enter student details below:")

# Input Section
name = st.text_input("Enter Student Name")

col1, col2 = st.columns(2)

with col1:
    sub1 = st.number_input("Math Marks", min_value=0, max_value=100)
    sub2 = st.number_input("Science Marks", min_value=0, max_value=100)
    sub3 = st.number_input("English Marks", min_value=0, max_value=100)

with col2:
    sub4 = st.number_input("Computer Marks", min_value=0, max_value=100)
    sub5 = st.number_input("Hindi Marks", min_value=0, max_value=100)

if st.button("Calculate Result"):

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    # Grade Logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Result Status
    if percentage >= 33:
        status = "Pass"
    else:
        status = "Fail"

    st.success("Result Calculated Successfully!")

    st.subheader("📊 Result Summary")
    st.write("Student Name:", name)
    st.write("Total Marks:", total)
    st.write("Percentage:", round(percentage, 2), "%")
    st.write("Grade:", grade)
    st.write("Status:", status)