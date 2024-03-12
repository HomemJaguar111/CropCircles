import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import Draw
from folium.plugins import HeatMap

from datetime import datetime

import plotly.express as px

import pandas as pd

st.set_page_config(layout='wide')
       
    ###############################################      
tempo = datetime.now()
anoA = tempo.year
mesA = tempo.month
diaA = tempo.day       
    ##############################################    
#Função que calcula o dia no Sincronário Maya    
def Kin(ano, mes, dia):    

    anocod = 0
    mescod = 0
    diacod = 0
    kin = 0
    
    
    if ano == 0 or ano % 52 == 0:
        anocod = 232
    elif ano == 1 or ano % 52 == 1:
        anocod = 77
    elif ano == 2 or ano % 52 == 2:
        anocod = 182
    elif ano == 3 or ano % 52 == 3:
        anocod = 27
    elif ano ==4 or ano % 52 == 4:
        anocod = 132
    elif ano ==5 or ano % 52 == 5:
        anocod = 237    
    elif ano ==6 or ano % 52 == 6:
        anocod = 82
    elif ano ==7 or ano % 52 == 7:
        anocod = 187
    elif ano ==8 or ano % 52 == 8:
        anocod = 32
    elif ano ==9 or ano & 52 == 9:
        anocod = 137
    elif ano ==10 or ano % 52 ==10: 
        anocod = 242
    elif ano ==11 or ano % 52 ==11: 
        anocod = 87
    elif ano ==12 or ano % 52 ==12: 
        anocod = 192
    elif ano ==13 or ano % 52 ==13: 
        anocod = 37
    elif ano ==14 or ano % 52 ==14: 
        anocod = 142
    elif ano ==15 or ano % 52 ==15: 
        anocod = 247
    elif ano ==16 or ano % 52 == 16:
        anocod = 92
    elif ano ==17 or ano % 52 == 17:
        anocod = 197 
    elif ano ==18 or ano % 52 == 18:
        anocod = 42
    elif ano ==19 or ano % 52 == 19:
        anocod = 147
    elif ano ==20 or ano % 52 == 20:
        anocod = 252
    elif ano ==21 or ano % 52 == 21:
        anocod = 97
    elif ano ==22 or ano % 52 == 22:
        anocod = 202
    elif ano ==23 or ano % 52 == 23:
        anocod = 47
    elif ano ==24 or ano & 52 == 24:
        anocod = 152
    elif ano ==25 or ano % 52 == 25:
        anocod = 257
    elif ano ==26 or ano % 52 == 26:
        anocod = 102
    elif ano ==27 or ano % 52 == 27:
        anocod = 207
    elif ano ==28 or ano % 52 == 28:
        anocod = 52
    elif ano ==29 or ano % 52 == 29:
        anocod = 157
    elif ano ==30 or ano % 52 == 30:
        anocod = 2
    elif ano ==31 or ano % 52 == 31:
        anocod = 107
    elif ano ==32 or ano % 52 == 32:
        anocod = 212 
    elif ano ==33 or ano % 52 == 33:
        anocod = 57
    elif ano ==34 or ano % 52 == 34:
        anocod = 162
    elif ano ==35 or ano % 52 == 35:
        anocod = 7
    elif ano ==36 or ano % 52 == 36:
        anocod = 112
    elif ano ==37 or ano % 52 == 37:
        anocod = 217
    elif ano ==38 or ano % 52 == 38:
        anocod = 62
    elif ano ==39 or ano & 52 == 39:
        anocod = 167
    elif ano ==40 or ano % 52 == 40:
        anocod = 12
    elif ano ==41 or ano % 52 == 41:
        anocod = 117
    elif ano ==42 or ano % 52 == 42:
        anocod = 222
    elif ano ==43 or ano % 52 == 43:
        anocod = 67
    elif ano ==44 or ano % 52 == 44:
        anocod = 172
    elif ano ==45 or ano % 52 == 45:
        anocod = 17
    elif ano ==46 or ano % 52 == 46:
        anocod = 122
    elif ano ==47 or ano % 52 == 47:
        anocod = 227
    elif ano ==48 or ano % 52 == 48:
        anocod = 72
    elif ano ==49 or ano & 52 == 49:
        anocod = 177
    elif ano ==50 or ano % 52 == 50:
        anocod = 22
    elif ano ==51 or ano % 52 == 51:
        anocod = 127
        
    if   mes == 1  : 
        mescod = 0
    elif mes == 2  : 
        mescod = 31
    elif mes == 3  : 
        mescod = 59
    elif mes == 4  : 
        mescod = 90
    elif mes == 5  : 
        mescod = 120
    elif mes == 6  : 
        mescod = 151
    elif mes == 7  : 
        mescod = 181
    elif mes == 8  : 
        mescod = 212
    elif mes == 9  : 
        mescod = 243
    elif mes == 10 : 
        mescod = 13
    elif mes == 11 : 
        mescod = 44
    elif mes == 12 : 
        mescod = 74


    if dia==1:
        diacod=1
    elif dia==2:
        diacod=2
    elif dia==3:
        diacod=3
    elif dia==4:
        diacod=4
    elif dia==5:
        diacod=5
    elif dia==6:
        diacod=6
    elif dia==7:
        diacod=7
    elif dia==8:
        diacod=8
    elif dia==9:
        diacod=9
    elif dia==10:
        diacod=10
    elif dia==11:
        diacod=11
    elif dia==12:
        diacod=12
    elif dia==13:
        diacod=13
    elif dia==14:
        diacod=14
    elif dia==15:
        diacod=15
    elif dia==16:
        diacod=16
    elif dia==17:
        diacod=17
    elif dia==18:
        diacod=18
    elif dia==19:
        diacod=19
    elif dia==20:
        diacod=20
    elif dia==21:
        diacod=21
    elif dia==22:
        diacod=22
    elif dia==23:
        diacod=23
    elif dia==24:
        diacod=24
    elif dia==25:
        diacod=25
    elif dia==26:
        diacod=26
    elif dia==27:
        diacod=27
    elif dia==28:
        diacod=28
    elif dia==29:
        diacod=29
    elif dia==30:
        diacod=30
    elif dia==31:
        diacod=31    
        
    codKin = anocod + mescod +diacod
    
    if codKin > 260:
        kin = codKin-260
    else:
        kin = codKin
        
    return kin

def main():    
    
    #Lendo os arquivos
    cropData= pd.read_csv('CropCircles.csv') 
    #Mapa Definido  ###############################################
    m = folium.Map(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')  
    
    #Controle de Camadas
    #folium.LayerControl(position="topleft").add_to(m)
            
    ###############################################################
     #Coordenadas
    loc=cropData['Locate']
    lat= cropData['Latitude']
    lon = cropData['Longitude']   
    
    #################################################################
   
    ########################################################
    
    cropData["Kin"] = cropData.apply(lambda row: Kin(row["Year"], row["Month"], row["Day"]), axis=1)
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
    st.write(Kin(ano=anoA,mes=mesA,dia=diaA))
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
