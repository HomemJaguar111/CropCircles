import streamlit as st
import folium
from folium.plugins import Draw
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import pandas as pd




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
    #Chamando as tabelas no site
    #dataset dos Crops
    
    
    ##############################################    
    #definições do mapa de monumentos
    loc=cropData['Locate']
    lat= cropData['Latitude']
    lon = cropData['Longitude']    
    
   
    
    #Adicionando função de calor no mapa
    coordTotal = cropData[["Latitude","Longitude"]].values.tolist()
    HeatMap(coordTotal, radius=50).add_to(m)
      
    ########################################################################
   
    
    ############################################################
    #Localizações dos Crops no mapa
    for c, la, lo in zip(loc, lat, lon):
        folium.Marker([la,lo], tooltip=c).add_to(m)       
    #Desenhar no mapa   
    #Draw().add_to(m)
    ###################################################################
    
    #####################################################################
    #Chamadas no Site
    
    #Título do site
    st.title("Localização dos Crop Circles")
    
    #Mapa Principal
    #return m
    folium_static(m)  
    #dataseet
    cropData        
    ##################################################################
if __name__ == "__main__":
    main()