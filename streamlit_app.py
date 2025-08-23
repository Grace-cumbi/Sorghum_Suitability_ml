import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.header('Random Forest Classification Model for Assessing Land Suitable for Sorghum Production')
m = folium.Map(location = [36.8152700, 0.2945864], zoom_start= 5)
folium.Marker(
  [36.8152700, 0.2945864], popup="Laikipia"
).add_to(m)
df = pd.read_csv('https://raw.githubusercontent.com/Grace-cumbi/Sorghum_Suitability_ml/refs/heads/master/Data1.csv')
st_data = st_folium(m, width=700, height=500)
st.image("https://github.com/Grace-cumbi/Sorghum_Suitability_ml/blob/master/final.png?raw=true")
st.write('Laikipia County Sorghum Poduction Suitability Map')
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
st.image("https://github.com/Grace-cumbi/Sorghum_Suitability_ml/blob/master/Reference.jpg?raw=true")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
rf = RandomForestClassifier()
rf.fit(X_train,y_train)
if st.button("Predict"):
  prediction = rf.predict(input_suitability)
  st.success(f'The predicted value is: {prediction[0]}') 
  
st.write("Feature Importance")
st.image("https://github.com/Grace-cumbi/Sorghum_Suitability_ml/blob/master/feature%20importance.png?raw=true")

 
