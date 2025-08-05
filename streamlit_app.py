import streamlit as st
import pandas as pd

st.title('Random Forest Classification Model for Assessing Land Suitable for Sorghum Production')
st.image("https://github.com/Grace-cumbi/Sorghum_Suitability_ml/blob/master/Sorghum.png.jpg?raw=true")
st.write('Sorghum bicolor')
with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Grace-cumbi/Sorghum_Suitability_ml/refs/heads/master/Data1.csv')
  df

st.write('**X**')
X = df.drop(columns = ['x','y','Suitability'])
X

st.write('**y**')
y = df.Suitability

with st.sidebar:
  st.header('Input Features')
  Temperature = st.selectbox('Temperature', (1,2,3,4))
  lulc = st.selectbox('LULC',(1,2,3,4))
  Annual_Rainfall = st.selectbox('Rainfall', (1,2,3,4))
  Slope = st.selectbox('Slope', (1,2,3,4))
  Land_Surface_Temperature= st.selectbox('LST', (1,2,3,4))
  Soil_PH = st.selectbox('PH', (1,2,3,4))
  Soil_Carbon = st.selectbox('Carbon', (1,2,3,4))
  Digital_Elevation_Model = st.selectbox('DEM', (1,2,3,4))
  NDVI = st.selectbox('NDVI', (1,2,3,4))
  Soil_Texture = st.selectbox('Texture', (1,2,3,4))
  Soil_Nitrogen = st.selectbox('Nitrogen', (1,2,3,4))
  Cation_Exchange_Capacity = st.selectbox('CEC', (1,2,3,4))
