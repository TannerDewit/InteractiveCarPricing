# -*- coding: utf-8 -*-
"""CarPricing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uYazy9KZUBEXpPRIP1JPRi7rANmqfyEJ
"""

import streamlit as st
import pandas as pd

@st.cache
def load_data():
  df=pd.read_csv('car_data.csv')
  return df



df=load_data()

st.title('Interactive Car Pricing Dashboard')

condition=st.radio('New or Used Car',['New','Used'])
year=st.selectbox('Select a Model Year', df['Year'].unique())

filtered_cars=df[(df['Status']==condition)&(df['Year']==year)]

st.write('Filtered Cars')
st.write(filtered_cars)