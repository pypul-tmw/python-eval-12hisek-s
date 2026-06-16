import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "size": [1000, 1200, 1500, 1800, 2000],
    "price": [200000, 240000, 300000, 360000, 400000]
})

x = data[["size"]]
y = data["price"]

model = LinearRegression()
model.fit(x, y)

st.title("House Price Predictor")

size = st.number_input(
    "Enter House Size",
    min_value=500
)

if st.button("Predict"):
    prediction = model.predict(
        pd.DataFrame({
            "size": [size]
        })
    )

    st.success(
        f"Predicted Price: ${prediction[0]:,.2f}"
    )