import streamlit as st
import pandas as pd

st.title("Hello. I'm a new user of streamlit.")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age: ",0,100,25)

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language", options)

if name:
    st.write(f"Hello, my name is {name}. I'm {age} years old. I love {choice}")


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

