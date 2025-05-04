import streamlit as st
import pandas as pd
from joblib import load

lgr = load('lgr_model.job')

st.title('Gender Classification')

with st.form(key='my_form'):
    st.image('banner.jpg', use_container_width=True)
    height = st.number_input(label='Enter height in cm')
    weight = st.number_input(label='Enter weight in kg')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if 75 < height < 250 and 20 < weight < 200:
            new_data_df = pd.DataFrame([[height, weight]], columns=lgr.feature_names_in_)
            pred = lgr.predict(new_data_df)[0]
            st.success(f'Gender is classified as **{pred}**')
        else:
            st.error('Invalid height and/or weight. Please re-enter the data.')
