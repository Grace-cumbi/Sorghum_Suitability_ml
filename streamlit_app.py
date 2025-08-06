import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

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
  y

with st.sidebar:
  st.header('Input Features')
  Temp = st.selectbox('Mean Annual Temperature', (1,2,3,4))
  LULC = st.selectbox('Land Use Land Cover (LULC)',(1,2,3,4))
  Rainfall = st.selectbox('Annual Rainfall', (1,2,3,4))
  Slope = st.selectbox('Slope', (1,2,3,4))
  LST = st.selectbox('Land Surface Temperature (LST)', (1,2,3,4))
  PH = st.selectbox('Soil PH', (1,2,3,4))
  Carbon = st.selectbox('Soil Carbon', (1,2,3,4))
  DEM = st.selectbox('Digital Elevation Model (DEM)', (1,2,3,4))
  NDVI = st.selectbox('Normalized Dense Vegetation Index (NDVI)', (1,2,3,4))
  Texture = st.selectbox(' Soil Texture', (1,2,3,4))
  Nitrogen = st.selectbox('Soil Nitrogen', (1,2,3,4))
  CEC = st.selectbox('Cation Exchange Capacity (CEC)', (1,2,3,4))

  data = {'Texture': Texture,
          'PH': PH,
          'CEC': CEC,
          'Nitrogen': Nitrogen,
          'Carbon': Carbon,
          'Temp': Temp,
          'Rainfall': Rainfall,
          'Slope': Slope,
          'DEM': DEM,
          'NDVI': NDVI,
          'LULC': LULC,
          'LST': LST,}
  input_df = pd.DataFrame(data, index=[0])
  input_suitability = pd.concat([input_df, X], axis=0)

input_df

clf = RandomForestClassifier()
clf.fit(X,y)
if st.button("Predict"):
  prediction = clf.predict(X)
 
  

  
