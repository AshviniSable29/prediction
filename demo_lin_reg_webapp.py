import streamlit as st
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Streamlit demo")

st.sidebar.header("This is a web app")

cgpa = st.sidebar.slider("Select cgpa to get salary", 0, 10, 5)

st.write("cgpa is:", cgpa)

salary = model.predict([[cgpa]])

st.write("b0 is", round(model.intercept_, 3))
st.write("b1 is", round(model.coef_[0], 3))
st.write("salary is", salary)
