import streamlit as st
from joblib import load

lgr = load('lgr_model.job')

st.title('Gender Classification')

with st.form(key='my_form'):
    st.image('banner.jpg', use_column_width=True)
    height = st.number_input(label='Enter height in cm')
    weight = st.number_input(label='Enter weight in kg')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if 75 < height < 250 and 20 < weight < 200:
            pred = lgr.predict([[height, weight]])[0]
            st.success(f'Gender is classified as **{pred}**')
        else:
            st.error('Invalid height and/or weight. Please re-enter the data.')
