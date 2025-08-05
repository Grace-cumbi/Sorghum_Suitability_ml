import streamlit as st
import pandas as pd

st.title('Random Forest Classification Model for Assessing Land Suitable for Sorghum Production')
st.image("https://github.com/Grace-cumbi/Sorghum_Suitability_ml/blob/master/Sorghum.png.jpg?raw=true")
st.write('Sorghum bicolor')
with st.expander("Data"):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Grace-cumbi/Sorghum_Suitability_ml/refs/heads/master/Data1.csv')
  df
  class = 1,2,3,4
with st.sidebar:
  st.header('Input Features')
  with st.expander('Temperature')
    st.write ('**Temperature**')
    class
  Temperature = st.expander('Temperature', 1,2,3,4)
  LULC = st.expander('LULC', 1,2,3,4)
  Annual_Rainfall = st.expander('Rainfall', 1,2,3,4)
  Slope = st.expander('Slope', 1,2,3,4)
  Land_Surface_Temperature= st.expander('LST', 1,2,3,4)
  Soil_PH = st.expander('PH', 1,2,3,4)
  Soil_Carbon = st.expander('Carbon', 1,2,3,4)
  Digital_Elevation_Model = st.expander('DEM', 1,2,3,4)
  NDVI = st.expander('NDVI', 1,2,3,4)
  Soil_Texture = st.expander('Texture', 1,2,3,4)
  Soil_Nitrogen = st.expander('Nitrogen',1,2,3,4)
  Cation_Exchange_Capacity = st.expander('CEC', 1,2,3,4)
