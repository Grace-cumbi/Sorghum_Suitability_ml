import streamlit as st
import pandas as pd

st.title('Random Forest Classification Model for Assessing Land Suitable for Sorghum Production')

st.write('Sorghum bicolor')
df = pd.read_csv('https://raw.githubusercontent.com/Grace-cumbi/Sorghum_Suitability_ml/refs/heads/master/Data1.csv')
df1 = pd.read_csv('https://raw.githubusercontent.com/Grace-cumbi/Sorghum_Suitability_ml/refs/heads/master/Refence.csv')
df
df1
