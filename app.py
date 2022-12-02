import streamlit as st
import pickle
import sklearn
model = pickle.load(open("medical_insurance.sav","rb"))
st.title("Medical insurance prediction")
age=st.text_input("Enter a Age")
col1,col2=st.columns(2)
with col1:
    st.write('Male-----> 0')
    st.write('Female-----> 1')
    sex=st.text_input('''Enter a sex ''')
with col2:
    st.write('Yes----->0')
    st.write('No----->1')
    smoker=st.text_input("Are you smoker")
col3,col4=st.columns(2)
with col3:
    bmi=st.text_input("BMI value")
with col4:
    children=st.text_input("Number of Children")
st.write('southeast-->0,southwest-->1,northeast --> 2,northwest ----->3')
region=st.text_input("Region ")

prediction=''
if st.button('predict'):
    prediction = model .predict([[age,sex,bmi,children,smoker,region]])
    st.write(prediction)
