import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.header('Random Forest Classification Model for Assessing Land Suitable for Sorghum Production')
df = pd.read_csv('https://raw.githubusercontent.com/Grace-cumbi/Sorghum_Suitability_ml/refs/heads/master/Data1.csv')
m = folium.Map(location = [df.iloc[0]['y'], df.iloc[0]['x']], zoom_start= 12)

folium.Marker(
  [0.2945864, 36.815270], 
  popup="Laikipia",
  icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

for index, row in df.iterrows():
    if row['Suitability'] == 4:
        color = 'green'  
    elif row['Suitability'] == 3:
        color = 'lightgreen'  
    elif row['Suitability'] == 2:
        color = 'yellow' 
    else:  # Suitability 1
        color = 'red' 
    
    folium.CircleMarker(
    location=[row['y'], row['x']],
    radius=2,
    popup=f"Suitability: {row['Suitability']}",
    color=color,
    fill=True,
    fillColor=color,
    fillOpacity=0.1
          ).add_to(m)
  
legend_html = '''
<div style="position: fixed; 
     bottom: 50px; right: 50px; width: 180px; height: 140px; 
     background-color: white; border:2px solid grey; z-index:9999;
     font-size:14px; padding: 10px; border-radius: 5px;">
     <b>Suitability Legend</b><br>
     <i style="background: green; width: 15px; height: 15px; 
        display: inline-block; border: 1px solid grey;"></i> Highly Suitable (4)<br>
     <i style="background: lightgreen; width: 15px; height: 15px; 
        display: inline-block; border: 1px solid grey;"></i> Moderately Suitable (3)<br>
     <i style="background: yellow; width: 15px; height: 15px; 
        display: inline-block; border: 1px solid grey;"></i> Marginally Suitable (2)<br>
     <i style="background: red; width: 15px; height: 15px; 
        display: inline-block; border: 1px solid grey;"></i> Not Suitable (1)
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))
st_data = st_folium(m, width=900, height=500)
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
  
st.write("Map Legend")
st.markdown("""
- <span style="color:green">**Green**</span>:Highly Suitable
- <span style="color:lightgreen">**Light Green**</span>:Moderately Suitable
- <span style="color:orange">**yellow**</span>:Marginally Suitable
- <span style="color:red">**Red**</span>:Not Suitable
""", unsafe_allow_html=True)

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
    prediction_value = prediction[0]
    if prediction_value == 4:
        prediction_text = "Highly Suitable"
        color = "green"
    elif prediction_value == 3:
        prediction_text = "Moderately Suitable"
        color = "lightgreen"
    elif prediction_value == 2:
        prediction_text = "Marginally Suitable"
        color = "yellow"
    else:  # prediction_value == 1
        prediction_text = "Not Suitable"
        color = "red"
    st.success(f'The predicted suitability is:{prediction_text}') 
  
st.write("Feature Importance")
st.image("https://github.com/Grace-cumbi/Sorghum_Suitability_ml/blob/master/feature%20importance.png?raw=true")

 
