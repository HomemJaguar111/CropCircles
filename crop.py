import streamlit as st
import folium
from folium.plugins import Draw
from folium.plugins import HeatMap
from streamlit_folium import folium_static


import plotly.express as px

import pandas as pd

st.set_page_config(layout='wide')

def main():
    #Mapa Definido  ###############################################
    m = folium.Map(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')  
    
    #Controle de Camadas
    #folium.LayerControl(position="topleft").add_to(m)
            
    ###############################################################
        
    #################################################################
    #Lendo os arquivos
    cropData= pd.read_csv('CropCircles.csv')
       
    ###############################################     
       
    ##############################################    
    #Coordenadas
    loc=cropData['Locate']
    lat= cropData['Latitude']
    lon = cropData['Longitude']    
    ########################################################
   
    #######################################################
    
    #Adicionando função de calor no mapa
    coordTotal = cropData[["Latitude","Longitude"]].values.tolist()
    HeatMap(coordTotal, radius=52).add_to(m)
      
    ########################################################################
       
    ############################################################
    #Localizações dos Crops no mapa
    for c, la, lo in zip(loc, lat, lon):
        folium.Marker([la,lo], tooltip=c).add_to(m)       
    #Desenhar no mapa   
    #Draw().add_to(m)
    ###################################################################
    
    #####################################################################
    #Gráficos
        
    #Gráfico em Pizza dos Paízes
    cropCountry = cropData['Country'].value_counts()
    pieCountryCrops = px.pie(cropCountry, 
                  values=cropCountry.values, 
                  names=cropCountry.index, 
                  title='Crop Circles por país')
    
    # Gráfico em Barra - Crops por Ano     
    yearCrops = cropData[["Year","Country"]].value_counts().reset_index()
    yearCropsBar = px.bar(yearCrops, 
                       x="Year",
                       y="count",
                       color="Country",
                       title="Crops em cada ano")
    
    #########################################################################
   
    #############################################################
    #Chamadas no Site
    
    #Título do site
    st.title("Localização dos Crop Circles")
    
    #Mapa Principal    
    folium_static(m)  
    #Gráfico em Pizza de Crops por País
    pieCountryCrops
    #Gráfico de Barras - Crops por Ano        
    yearCropsBar
    #dataset
    cropData        
    ##################################################################
if __name__ == "__main__":
    main()