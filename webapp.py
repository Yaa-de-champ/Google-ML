import streamlit as st
import joblib

model = joblib.load('RF_model.joblib')

st.title('Simple Web App')

st.write('This app takes two inputs')

SL = st.number_input('Enter Sepal Legth: ')
SW = st.number_input('Enter Sepal Width: ')
PL = st.number_input('Enter Petal Legth: ')
PW = st.number_input('Enter Petal Width : ')



if st.button('Predict'):
    prediction = model.predict([[SL, SW, PL, PW]])
    if prediction == 0:
        st.write('Iris Setosa')
        print
    elif prediction == 1:
        st.write('Iris Vesicolor')
    else:
        st.write('Iris Virginica')
