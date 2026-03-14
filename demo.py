import streamlit as st

st.title('Streamlit Demo')

email = st.text_input('Email')
password = st.text_input('Password')

btn = st.button('Login')
if btn:
    if email == 'sugatasaha104@gmail.com' and password == '1234':
        st.success('Login Successful')
    else:
        st.error('Login Unsuccessful')