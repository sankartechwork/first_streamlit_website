import streamlit as st
import pandas as pd
import numpy as np

st.title("My first Streamlit App")

name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello,{name}!")

age=st.slider("Select your age:",1,100)
st.write(f"You are {age} years old")

if st.button("Click Me"):
    st.write("Button Clicked!")

data=pd.DataFrame(np.random.randn(20,3),columns=["A","B","C"])
st.line_chart(data)

st.sidebar.title("Menu")
choice=st.sidebar.selectbox("Choose",["Home","About"])
if choice=="Home":
    st.write("Welcome")