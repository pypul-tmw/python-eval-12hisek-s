import streamlit as st 

st.title("BMI Calculator")

weight = st.number_input(
    "Weight (kg)",min_value = 1.0
)

height = st.number_input(
    "Height (m)",
    min_value = 0.1
)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write("BMI:",round(bmi,2))