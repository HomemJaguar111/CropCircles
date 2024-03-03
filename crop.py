!pip install folium 
import streamlit as st
import folium
from folium.plugins import Draw
from streamlit_folium import folium_static
import pandas as pd




def main():
    #Lendo os arquivos
    cropData= pd.read_csv('CropCircles.csv')
       
    ###############################################     
    #Chamando as tabelas no site
    #dataset dos Crops
    cropData
    
    ##############################################    
    #definições do mapa de monumentos
    loc=cropData['Locate']
    lat= cropData['Latitude']
    lon = cropData['Longitude']    
    #definição do index do mapa dos Crops
    
   
    #Mapas Definidos  ###############################################
    m = folium.Map(zoom_start=2)  
       
    #Draw().add_to(m)  
    ########################################################################
    #Adicionando minha localização no mapa    
    
    ############################################################
    #Mapa Crop 
    for c, la, lo in zip(loc, lat, lon):
        folium.Marker([la,lo], tooltip=c).add_to(m)       
    
    st.title("Mapa dos CropCircles")
    folium_static(m)          
    
if __name__ == "__main__":
    main()