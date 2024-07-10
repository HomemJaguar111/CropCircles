import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import Draw
from folium.plugins import HeatMap

from datetime import datetime

import plotly.express as px

import pandas as pd

st.set_page_config(layout='wide')

#Título do Site
st.title("Localização dos Crop Circles")   

#Mapas 
m = folium.Map(location=[52.19681,0.12901],zoom_start=7,tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',control_scale=True) 
mElement = folium.Map(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',control_scale=True)  
mPortal = folium.Map(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',control_scale=True)  
mAngels = folium.Map(location=[51.42692,18.93166],zoom_start=4.1,tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',control_scale=True)  
mPortalAngels =folium.Map(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',control_scale=True)  
    
    ###############################################      
tempo = datetime.now()
anoA = tempo.year
mesA = tempo.month
diaA = tempo.day       
    ##############################################    
#Funções   
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
def ElementKin(kin):
    if kin == 1 or kin % 4 == 1:
        element = "Fire"
    elif kin == 2 or kin % 4 == 2:
        element = "Air"
    elif kin == 3 or kin % 4 == 3:
        element = "Water"
    elif kin == 4 or kin % 4 == 0:
        element = "Ground"                        
    return element
def StampKin(kin):
    if kin == 1 or kin % 20 == 1:
        stamp = "Dragon"
    elif kin == 2 or kin % 20 ==2: 
        stamp = "Wind"
    elif kin == 3 or kin % 20 == 3:
        stamp = "Night"
    elif kin == 4 or kin % 20 == 4: 
        stamp = "Seed"
    elif kin == 5 or kin % 20 == 5: 
        stamp = "Serpent"
    elif kin == 6 or kin % 20 == 6: 
        stamp = "Link"
    elif kin == 7 or kin % 20 == 7: 
        stamp = "Hand"
    elif kin == 8 or kin % 20 == 8: 
        stamp = "Star"
    elif kin ==  9 or kin % 20 == 9: 
        stamp = "Moon"
    elif kin == 10 or kin % 20 == 10: 
        stamp = "Dog"
    elif kin == 11 or kin % 20 == 11: 
        stamp = "Monkey"
    elif kin == 12 or kin % 20 == 12: 
        stamp = "Human"
    elif kin == 13 or kin % 20 == 13: 
        stamp = "Sky Walker"
    elif kin == 14 or kin % 20 == 14: 
        stamp = "Wizard"
    elif kin == 15 or kin % 20 == 15:
        stamp = "Eagle"
    elif kin == 16 or kin % 20 == 16: 
        stamp = "Warrior"
    elif kin == 17 or kin % 20 == 17:
        stamp = "Earth"
    elif kin == 18 or kin % 20 == 18:
        stamp = "Mirror"
    elif kin == 19 or kin % 20 == 19:
        stamp = "Storm"
    elif kin == 20 or kin % 20 == 0: 
        stamp = "Sun"
    
    return stamp
def Portal(kin):
    
    if kin==1 or kin==20 or kin==22 or kin==39 or kin==43 or kin==50 or kin==51 or kin==58 or kin==64 or kin==69 or kin==72 or kin==77 or kin==85 or kin==88 or kin==93 or kin==96 or kin==106 or kin==107 or kin==108 or kin==109 or kin==110 or kin==111 or kin==112 or kin==113 or kin==114 or kin==115 or kin==146 or kin==147 or kin==149 or kin==150 or kin==151 or kin==152 or kin==153 or kin==154 or kin==155 or kin==165 or kin==168 or kin==173 or kin==176 or kin==184 or kin==189 or kin==192 or kin==197 or kin==203 or kin==210 or kin==211 or kin==218 or kin==222 or kin==239 or kin==241 or kin==260:
        gate = "Yes"
    else:
        gate = "No"
        
    return gate

def AngelsNum(mes, dia):
    angelNum = 0
    angelNam =''
    
    
    if dia == 1:
        if mes == 1:
            angelNum = 69            
        elif mes == 2:
            angelNum = 27
        elif mes == 3:
            angelNum = 55
        elif mes == 4:
            angelNum = 13
            
        elif mes == 5: 
            angelNum = 43
            
        elif mes == 6:
            angelNum = 1
            
        elif mes == 7:
            angelNum = 31
            
        elif mes == 8:
            angelNum = 62
            
        elif mes == 9:
            angelNum = 20
            
        elif mes == 10:
            angelNum = 50
            
        elif mes == 11: 
            angelNum = 8
            
        elif mes == 12:
            angelNum = 38
           
                    
    elif dia == 2:
        if mes == 1:
            angelNum = 70
            
        elif mes == 2:
            angelNum = 28
            
        elif mes == 3:
            angelNum = 56
            
        elif mes == 4:
            angelNum = 14
            
        elif mes == 5: 
            angelNum = 44
            
        elif mes == 6:
            angelNum = 2
            
        elif mes == 7:
            angelNum = 32
            
        elif mes == 8:
            angelNum = 63
            
        elif mes == 9:
            angelNum = 21
            
        elif mes == 10:
            angelNum = 51
            
        elif mes == 11: 
            angelNum = 8
            
        elif mes == 12:
            angelNum = 39
            
            
    elif dia == 3:
        if mes == 1:
            angelNum = 71
           
        elif mes == 2:
            angelNum = 29
            
        elif mes == 3:
            angelNum = 57
            
        elif mes == 4:
            angelNum = 15
            
        elif mes == 5: 
            angelNum = 45
           
        elif mes == 6:
            angelNum = 3
            
        elif mes == 7:
            angelNum = 33
            
        elif mes == 8:
            angelNum = 64
            
        elif mes == 9:
            angelNum = 22
            
        elif mes == 10:
            angelNum = 52
            
        elif mes == 11: 
            angelNum = 9
            
        elif mes == 12:
            angelNum = 40
           
            
    elif dia == 4:
        if mes == 1:
            angelNum = 72
           
        elif mes == 2:
            angelNum = 30
            
        elif mes == 3:
            angelNum = 58
            
        elif mes == 4:
            angelNum = 16
            
        elif mes == 5: 
            angelNum = 46
           
        elif mes == 6:
            angelNum = 4
            
        elif mes == 7:
            angelNum = 34
            
        elif mes == 8:
            angelNum = 65
            
        elif mes == 9:
            angelNum = 23
            
        elif mes == 10:
            angelNum = 53
            
        elif mes == 11: 
            angelNum = 10
            
        elif mes == 12:
            angelNum = 41
            
            
    elif dia == 5:
        if mes == 1:
            angelNum = 0
            
        elif mes == 2:
            angelNum = 31
            
        elif mes == 3:
            angelNum = 59
           
        elif mes == 4:
            angelNum = 17
            
        elif mes == 5: 
            angelNum = 47
            
        elif mes == 6:
            angelNum = 5
            
        elif mes == 7:
            angelNum = 35
            
        elif mes == 8:
            angelNum = 66
            
        elif mes == 9:
            angelNum = 24
            
        elif mes == 10:
            angelNum = 54
            
        elif mes == 11: 
            angelNum = 11
            
        elif mes == 12:
            angelNum = 42
            
            
    elif dia == 6:
        if mes == 1:
            angelNum = 1
            
        elif mes == 2:
            angelNum = 32
            
        elif mes == 3:
            angelNum = 60
            
        elif mes == 4:
            angelNum = 18
           
        elif mes == 5: 
            angelNum = 48
            
        elif mes == 6:
            angelNum = 6
            
        elif mes == 7:
            angelNum = 36
           
        elif mes == 8:
            angelNum = 67
            
        elif mes == 9:
            angelNum = 25
             
        elif mes == 10:
            angelNum = 55
            
        elif mes == 11: 
            angelNum = 12
            
        elif mes == 12:
            angelNum = 43
            
            
    elif dia == 7:
        if mes == 1:
            angelNum = 2
           
        elif mes == 2:
            angelNum = 33
            
        elif mes == 3:
            angelNum = 61
            
        elif mes == 4:
            angelNum = 19
            
        elif mes == 5: 
            angelNum = 49
            
        elif mes == 6:
            angelNum = 7
            
        elif mes == 7:
            angelNum = 37
            
        elif mes == 8:
            angelNum = 68
            
        elif mes == 9:
            angelNum = 26
            
        elif mes == 10:
            angelNum = 56
            
        elif mes == 11: 
            angelNum = 13
            
        elif mes == 12:
            angelNum = 44
            
            
    elif dia == 8:
        if mes == 1:
            angelNum = 3
            
        elif mes == 2:
            angelNum = 34
            
        elif mes == 3:
            angelNum = 62
            
        elif mes == 4:
            angelNum = 20
            
        elif mes == 5: 
            angelNum = 50
            
        elif mes == 6:
            angelNum = 8
            
        elif mes == 7:
            angelNum = 38
            
        elif mes == 8:
            angelNum = 69
            
        elif mes == 9:
            angelNum = 27
            
        elif mes == 10:
            angelNum = 57
            
        elif mes == 11: 
            angelNum = 14
            
        elif mes == 12:
            angelNum = 45
           
            
    elif dia == 9:
        if mes == 1:
            angelNum = 4
           
        elif mes == 2:
            angelNum = 35
           
        elif mes == 3:
            angelNum = 63
            
        elif mes == 4:
            angelNum = 21
          
        elif mes == 5: 
            angelNum = 51
            
        elif mes == 6:
            angelNum = 9
            
        elif mes == 7:
            angelNum = 39
            
        elif mes == 8:
            angelNum = 70
           
        elif mes == 9:
            angelNum = 28
           
        elif mes == 10:
            angelNum = 58
           
        elif mes == 11: 
            angelNum = 15
            
        elif mes == 12:
            angelNum = 46
            
            
    elif dia == 10:
        if mes == 1:
            angelNum = 5
            
        elif mes == 2:
            angelNum = 36
            
        elif mes == 3:
            angelNum = 64
            
        elif mes == 4:
            angelNum = 22
            
        elif mes == 5: 
            angelNum = 52
            
        elif mes == 6:
            angelNum = 10
            
        elif mes == 7:
            angelNum = 40
            
        elif mes == 8:
            angelNum = 71
            
        elif mes == 9:
            angelNum = 29
            
        elif mes == 10:
            angelNum = 59
            
        elif mes == 11: 
            angelNum = 16
            
        elif mes == 12:
            angelNum = 47
            
            
    elif dia == 11:
        if mes == 1:
            angelNum = 6
            
        elif mes == 2:
            angelNum = 37
            
        elif mes == 3:
            angelNum = 65
            
        elif mes == 4:
            angelNum = 23
            
        elif mes == 5: 
            angelNum = 53
           
        elif mes == 6:
            angelNum = 11
            
        elif mes == 7:
            angelNum = 41
           
        elif mes == 8:
            angelNum = 72
            
        elif mes == 9:
            angelNum = 30
            
        elif mes == 10:
            angelNum = 60
            
        elif mes == 11: 
            angelNum = 17
            
        elif mes == 12:
            angelNum = 48
            
            
            
    elif dia == 12:
        if mes == 1:
            angelNum = 7
            
        elif mes == 2:
            angelNum = 38
            
        elif mes == 3:
            angelNum = 66
            
        elif mes == 4:
            angelNum = 24
            
        elif mes == 5: 
            angelNum = 54
            
        elif mes == 6:
            angelNum = 12
            
        elif mes == 7:
            angelNum = 42
           
        elif mes == 8:
            angelNum = 0
            
        elif mes == 9:
            angelNum = 31
            
        elif mes == 10:
            angelNum = 61
            
        elif mes == 11: 
            angelNum = 18
            
        elif mes == 12:
            angelNum = 49
            
            
    elif dia == 13:
        if mes == 1:
            angelNum = 8
            
        elif mes == 2:
            angelNum = 39
            
        elif mes == 3:
            angelNum = 67
            
        elif mes == 4:
            angelNum = 25
           
        elif mes == 5: 
            angelNum = 55
            
        elif mes == 6:
            angelNum = 13
            
        elif mes == 7:
            angelNum = 43
            
        elif mes == 8:
            angelNum = 1
           
        elif mes == 9:
            angelNum = 32
            
        elif mes == 10:
            angelNum = 62
            
        elif mes == 11: 
            angelNum = 19
            
        elif mes == 12:
            angelNum = 50
            
            
    elif dia == 13:
        if mes == 1:
            angelNum = 8
            
        elif mes == 2:
            angelNum = 39
            
        elif mes == 3:
            angelNum = 67
           
        elif mes == 4:
            angelNum = 25
            
        elif mes == 5: 
            angelNum = 55
           
        elif mes == 6:
            angelNum = 13
            
        elif mes == 7:
            angelNum = 43
           
        elif mes == 8:
            angelNum = 1
            
        elif mes == 9:
            angelNum = 32
            
        elif mes == 10:
            angelNum = 62
           
        elif mes == 11: 
            angelNum = 19
            
        elif mes == 12:
            angelNum = 50
           
            
    elif dia == 14:
        if mes == 1:
            angelNum = 9
            
        elif mes == 2:
            angelNum = 40
            
        elif mes == 3:
            angelNum = 68
            
        elif mes == 4:
            angelNum = 26
            
        elif mes == 5: 
            angelNum = 56
            
        elif mes == 6:
            angelNum = 14
            
        elif mes == 7:
            angelNum = 44
            
        elif mes == 8:
            angelNum = 2
            
        elif mes == 9:
            angelNum = 33
            
        elif mes == 10:
            angelNum = 63
            
        elif mes == 11: 
            angelNum = 20
            
        elif mes == 12:
            angelNum = 51
            
            
    elif dia == 15:
        if mes == 1:
            angelNum = 10
            
        elif mes == 2:
            angelNum = 41
            
        elif mes == 3:
            angelNum = 69
            
        elif mes == 4:
            angelNum = 27
            
        elif mes == 5: 
            angelNum = 57
            
        elif mes == 6:
            angelNum = 15
            
        elif mes == 7:
            angelNum = 45
            
        elif mes == 8:
            angelNum = 3
            
        elif mes == 9:
            angelNum = 34
            
        elif mes == 10:
            angelNum = 64
           
        elif mes == 11: 
            angelNum = 21
            
        elif mes == 12:
            angelNum = 52
            
            
    elif dia == 16:
        if mes == 1:
            angelNum = 11
            
        elif mes == 2:
            angelNum = 42
            
        elif mes == 3:
            angelNum = 70
            
        elif mes == 4:
            angelNum = 28
            
        elif mes == 5: 
            angelNum = 58
            
        elif mes == 6:
            angelNum = 16
            
        elif mes == 7:
            angelNum = 46
            
        elif mes == 8:
            angelNum = 4
            
        elif mes == 9:
            angelNum = 35
            
        elif mes == 10:
            angelNum = 65
            
        elif mes == 11: 
            angelNum = 22
            
        elif mes == 12:
            angelNum = 53
            
            
    elif dia == 17:
        if mes == 1:
            angelNum = 12
            
        elif mes == 2:
            angelNum = 43
            
        elif mes == 3:
            angelNum = 71
            
        elif mes == 4:
            angelNum = 29
            
        elif mes == 5: 
            angelNum = 59
            
        elif mes == 6:
            angelNum = 17
            
        elif mes == 7:
            angelNum = 47
            
        elif mes == 8:
            angelNum = 5
            
        elif mes == 9:
            angelNum = 36
            
        elif mes == 10:
            angelNum = 66
            
        elif mes == 11: 
            angelNum = 23
            
        elif mes == 12:
            angelNum = 54
            
            
    elif dia == 18:
        if mes == 1:
            angelNum = 13
            
        elif mes == 2:
            angelNum = 44
            
        elif mes == 3:
            angelNum = 72
            
        elif mes == 4:
            angelNum = 30
            
        elif mes == 5: 
            angelNum = 60
            
        elif mes == 6:
            angelNum = 18
            
        elif mes == 7:
            angelNum = 48
            
        elif mes == 8:
            angelNum = 6
            
        elif mes == 9:
            angelNum = 37
            
        elif mes == 10:
            angelNum = 67
            
        elif mes == 11: 
            angelNum = 24
            
        elif mes == 12:
            angelNum = 55
            
            
    elif dia == 19:
        if mes == 1:
            angelNum = 14
            
        elif mes == 2:
            angelNum = 45
            
        elif mes == 3:
            angelNum = 0
            
        elif mes == 4:
            angelNum = 31
            
        elif mes == 5: 
            angelNum = 61
            
        elif mes == 6:
            angelNum = 19
            
        elif mes == 7:
            angelNum = 49
            
        elif mes == 8:
            angelNum = 7
            
        elif mes == 9:
            angelNum = 38
            
        elif mes == 10:
            angelNum = 68
            
        elif mes == 11: 
            angelNum = 25
            
        elif mes == 12:
            angelNum = 56
            
            
    elif dia == 20:
        if mes == 1:
            angelNum = 15
            
        elif mes == 2:
            angelNum = 46
            
        elif mes == 3:
            angelNum = 1
            
        elif mes == 4:
            angelNum = 32
            
        elif mes == 5: 
            angelNum = 62
            
        elif mes == 6:
            angelNum = 20
            
        elif mes == 7:
            angelNum = 50
            
        elif mes == 8:
            angelNum = 8
            
        elif mes == 9:
            angelNum = 39
            
        elif mes == 10:
            angelNum = 69
            
        elif mes == 11: 
            angelNum = 26
            
        elif mes == 12:
            angelNum = 57
            
            
    elif dia == 21:
        if mes == 1:
            angelNum = 16
            
        elif mes == 2:
            angelNum = 47
            
        elif mes == 3:
            angelNum = 2
            
        elif mes == 4:
            angelNum = 33
            
        elif mes == 5: 
            angelNum = 63
            
        elif mes == 6:
            angelNum = 21
            
        elif mes == 7:
            angelNum = 51
            
        elif mes == 8:
            angelNum = 9
            
        elif mes == 9:
            angelNum = 40
            
        elif mes == 10:
            angelNum = 70
            
        elif mes == 11: 
            angelNum = 27
            
        elif mes == 12:
            angelNum = 58
            
            
    elif dia == 22:
        if mes == 1:
            angelNum = 17
            
        elif mes == 2:
            angelNum = 48
            
        elif mes == 3:
            angelNum = 3
            
        elif mes == 4:
            angelNum = 34
            
        elif mes == 5: 
            angelNum = 64
            
        elif mes == 6:
            angelNum = 22
            
        elif mes == 7:
            angelNum = 52
            
        elif mes == 8:
            angelNum = 10
            
        elif mes == 9:
            angelNum = 41
            
        elif mes == 10:
            angelNum = 71
            
        elif mes == 11: 
            angelNum = 28
            
        elif mes == 12:
            angelNum = 59
            
            
    elif dia == 23:
        if mes == 1:
            angelNum = 18
            
        elif mes == 2:
            angelNum = 49
            
        elif mes == 3:
            angelNum = 4
            
        elif mes == 4:
            angelNum = 35
            
        elif mes == 5: 
            angelNum = 65
            
        elif mes == 6:
            angelNum = 23
            
        elif mes == 7:
            angelNum = 53
            
        elif mes == 8:
            angelNum = 11
            
        elif mes == 9:
            angelNum = 42
            
        elif mes == 10:
            angelNum = 72
            
        elif mes == 11: 
            angelNum = 29
            
        elif mes == 12:
            angelNum = 60
            
            
    elif dia == 24:
        if mes == 1:
            angelNum = 19
            
        elif mes == 2:
            angelNum = 50
            
        elif mes == 3:
            angelNum = 5
            
        elif mes == 4:
            angelNum = 36
            
        elif mes == 5: 
            angelNum = 66
            
        elif mes == 6:
            angelNum = 24
            
        elif mes == 7:
            angelNum = 54
            
        elif mes == 8:
            angelNum = 12
            
        elif mes == 9:
            angelNum = 43
            
        elif mes == 10:
            angelNum = 0
            
        elif mes == 11: 
            angelNum = 30
            
        elif mes == 12:
            angelNum = 61
            
            
    elif dia == 25:
        if mes == 1:
            angelNum = 20
            
        elif mes == 2:
            angelNum = 51
            
        elif mes == 3:
            angelNum = 6
            
        elif mes == 4:
            angelNum = 37
            
        elif mes == 5: 
            angelNum = 67
            
        elif mes == 6:
            angelNum = 25
            
        elif mes == 7:
            angelNum = 55
            
        elif mes == 8:
            angelNum = 13
            
        elif mes == 9:
            angelNum = 44
            
        elif mes == 10:
            angelNum = 1
            
        elif mes == 11: 
            angelNum = 31
            
        elif mes == 12:
            angelNum = 62
            
            
    elif dia == 26:
        if mes == 1:
            angelNum = 21
            
        elif mes == 2:
            angelNum = 52
            
        elif mes == 3:
            angelNum = 7
            
        elif mes == 4:
            angelNum = 38
            
        elif mes == 5: 
            angelNum = 68
            
        elif mes == 6:
            angelNum = 26
            
        elif mes == 7:
            angelNum = 56
            
        elif mes == 8:
            angelNum = 14
            
        elif mes == 9:
            angelNum = 45
            
        elif mes == 10:
            angelNum = 2
            
        elif mes == 11: 
            angelNum = 32
            
        elif mes == 12:
            angelNum = 63
            
            
    elif dia == 27:
        if mes == 1:
            angelNum = 22
            
        elif mes == 2:
            angelNum = 53
            
        elif mes == 3:
            angelNum = 8
            
        elif mes == 4:
            angelNum = 39
            
        elif mes == 5: 
            angelNum = 69
            
        elif mes == 6:
            angelNum = 27
            
        elif mes == 7:
            angelNum = 57
            
        elif mes == 8:
            angelNum = 15
            
        elif mes == 9:
            angelNum = 46
            
        elif mes == 10:
            angelNum = 3
            
        elif mes == 11: 
            angelNum = 33
            
        elif mes == 12:
            angelNum = 64
            
            
    elif dia == 28:
        if mes == 1:
            angelNum = 23
            
        elif mes == 2:
            angelNum = 54
            
        elif mes == 3:
            angelNum = 9
            
        elif mes == 4:
            angelNum = 40
            
        elif mes == 5: 
            angelNum = 70
            
        elif mes == 6:
            angelNum = 28
            
        elif mes == 7:
            angelNum = 58
            
        elif mes == 8:
            angelNum = 16
            
        elif mes == 9:
            angelNum = 47
            
        elif mes == 10:
            angelNum = 4
            
        elif mes == 11: 
            angelNum = 34
            
        elif mes == 12:
            angelNum = 65
            
            
    elif dia == 29:
        if mes == 1:
            angelNum = 24
            
        elif mes == 2:
            angelNum = 55
            
        elif mes == 3:
            angelNum = 10
            
        elif mes == 4:
            angelNum = 41
            
        elif mes == 5: 
            angelNum = 71
            
        elif mes == 6:
            angelNum = 29
            
        elif mes == 7:
            angelNum = 59
            
        elif mes == 8:
            angelNum = 17
            
        elif mes == 9:
            angelNum = 48
            
        elif mes == 10:
            angelNum = 5
            
        elif mes == 11: 
            angelNum = 35
            
        elif mes == 12:
            angelNum = 66
            
            
    elif dia == 30:
        if mes == 1:
            angelNum = 25
            
        elif mes == 2:
            angelNum = 56
            
        elif mes == 3:
            angelNum = 11
            
        elif mes == 4:
            angelNum = 42
            
        elif mes == 5: 
            angelNum = 72
            
        elif mes == 6:
            angelNum = 30
            
        elif mes == 7:
            angelNum = 60
            
        elif mes == 8:
            angelNum = 18
            
        elif mes == 9:
            angelNum = 49
            
        elif mes == 10:
            angelNum = 6
            
        elif mes == 11: 
            angelNum = 36
            
        elif mes == 12:
            angelNum = 67
            
            
    elif dia == 31:
        if mes == 1:
            angelNum = 26
            
        elif mes == 2:
            angelNum = 57
            
        elif mes == 3:
            angelNum = 12
            
        elif mes == 4:
            angelNum = 43
            
        elif mes == 5: 
            angelNum = 0
            
        elif mes == 6:
            angelNum = 31
            
        elif mes == 7:
            angelNum = 61
            
        elif mes == 8:
            angelNum = 19
            
        elif mes == 9:
            angelNum = 50
            
        elif mes == 10:
            angelNum = 7
            
        elif mes == 11: 
            angelNum = 37
            
        elif mes == 12:
            angelNum = 68
            
    

    
    
    return angelNum #,angelNam  
def AngelsNam(angelNum):
    
    if angelNum == 0:
        angelNam ="Emmanuel"
    elif angelNum == 1:
        angelNam ="Vehuiah"
    elif angelNum == 2:
        angelNam ="Jeliel"
    elif angelNum == 3:
        angelNam ="Sitael"
    elif angelNum == 4:
        angelNam ="Elemiah"
    elif angelNum == 5:
        angelNam ="Mahasiah"
    elif angelNum == 6:
        angelNam ="Lelahel"
    elif angelNum == 7:
        angelNam ="Achaiah"
    elif angelNum == 8:
        angelNam ="Cahetel"
    elif angelNum == 9:
        angelNam ="Haziel"
    elif angelNum == 10:
        angelNam ="Aladiah"
    elif angelNum == 11:
        angelNam ="Laoviah"
    elif angelNum == 12:
        angelNam ="Hahahiah"
    elif angelNum == 13:
        angelNam ="Yesalel"
    elif angelNum == 14:
        angelNam ="Mebahel"
    elif angelNum == 15:
        angelNam ="Hariel"
    elif angelNum == 16:
        angelNam ="Hekamiah"
    elif angelNum == 17:
        angelNam ="Lauviah"
    elif angelNum == 18:
        angelNam ="Caliel"
    elif angelNum == 19:
        angelNam ="Leuviah"
    elif angelNum == 20:
        angelNam ="Pahaliah"
    elif angelNum == 21:
        angelNam ="Nelchael"
    elif angelNum == 22:
        angelNam ="Ieiaiel"
    elif angelNum == 23:
        angelNam ="Melahel"
    elif angelNum == 24:
        angelNam ="Hahehuiah"
    elif angelNum == 25:
        angelNam ="Nith-Haiah"
    elif angelNum == 26:
        angelNam ="Haaiah"
    elif angelNum == 27:
        angelNam ="Ierathel"
    elif angelNum == 28:
        angelNam ="Seheiah"
    elif angelNum == 29:
        angelNam ="Reyel"
    elif angelNum == 30:
        angelNam ="Omael"
    elif angelNum == 31:
        angelNam ="Lecabel"
    elif angelNum == 32:
        angelNam ="Vasariah"
    elif angelNum == 33:
        angelNam ="Iehuiah"
    elif angelNum == 34:
        angelNam ="Lehahiah"
    elif angelNum == 35:
        angelNam ="Chavakiah"
    elif angelNum == 36:
        angelNam ="Menadel"
    elif angelNum == 37:
        angelNam ="Aniel"
    elif angelNum == 38:
        angelNam ="Haamiah"
    elif angelNum == 39:
        angelNam ="Hehael"
    elif angelNum == 40:
        angelNam ="Ieiazel"
    elif angelNum == 41:
        angelNam ="Hahahel"
    elif angelNum == 42:
        angelNam ="Mikael"
    elif angelNum == 43:
        angelNam ="Veuliah"
    elif angelNum == 44:
        angelNam ="Yelaiah"
    elif angelNum == 45:
        angelNam ="Sealiah"
    elif angelNum == 46:
        angelNam ="Ariel"
    elif angelNum == 47:
        angelNam ="Asaliah"
    elif angelNum == 48:
        angelNam ="Mihael"
    elif angelNum == 49:
        angelNam ="Vehuel"
    elif angelNum == 50:
        angelNam ="Daniel"
    elif angelNum == 51:
        angelNam ="Hahasiah"
    elif angelNum == 52:
        angelNam ="Imamaiah"
    elif angelNum == 53:
        angelNam ="Nanael"
    elif angelNum == 54:
        angelNam ="Nitael"
    elif angelNum == 55:
        angelNam ="Mebahiah"
    elif angelNum == 56:
        angelNam ="Poiel"
    elif angelNum == 57:
        angelNam ="Nemamiah"
    elif angelNum == 58:
        angelNam ="Ieialel"
    elif angelNum == 59:
        angelNam ="Harahel"
    elif angelNum == 60:
        angelNam ="Mitzrael"
    elif angelNum == 61:
        angelNam ="Umabel"
    elif angelNum == 62:
        angelNam ="Iah-hel"
    elif angelNum == 63:
        angelNam ="Anauel"
    elif angelNum == 64:
        angelNam ="Mehiel"
    elif angelNum == 65:
        angelNam ="Damabiah"
    elif angelNum == 66:
        angelNam ="Manakel"
    elif angelNum == 67:
        angelNam ="Ayel"
    elif angelNum == 68:
        angelNam ="Habuhiah"
    elif angelNum == 69:
        angelNam ="Rochel"
    elif angelNum == 70:
        angelNam ="Yamabiah"
    elif angelNum == 71:
        angelNam ="Haiael"
    elif angelNum == 72:
        angelNam ="Mumiah"
         
    return angelNam
def AngelsHierarchy(angelNum):
    if angelNum <= 8:
        hierarchy = "Serafins"
    elif angelNum <= 16:
        hierarchy = "Cherubins"
    elif angelNum <= 24:
        hierarchy = "Ophanim"
    elif angelNum <= 32:
        hierarchy = "Dominions"
    elif angelNum <= 40:
        hierarchy = "Powers"
    elif angelNum <= 48:
        hierarchy = "Virtues"
    elif angelNum <= 56:
        hierarchy = "Rulers"
    elif angelNum <= 64:
        hierarchy = "Archangels"
    else:
        hierarchy = "Angels"
        
    return hierarchy
    
def main():    
    ###################################################
    #Criando as tabelas    
    
    #Tabela CropCircles
    cropData= pd.read_csv('CropCircles.csv')      
    #Controle de Camadas
    #folium.LayerControl(position="topleft").add_to(m)
            
    ###############################################################
      
    ########################################################
    #Inserindo novas colunas na tabela
    
    #Coluna dos Kins Maya
    cropData["Kin"] = cropData.apply(lambda row: Kin(row["Year"], row["Month"], row["Day"]), axis=1)
        
    #Coluna dos Elementos Kin
    cropData["Element Kin"] = cropData.apply(lambda row: ElementKin(row["Kin"]), axis=1)
    
    #Coluna dos Selos Maia
    cropData["Stamp"]= cropData.apply(lambda row: StampKin(row["Kin"]), axis=1)
    
    #Coluna dos 52 Portais Maia
    cropData["Gate"] = cropData.apply(lambda row: Portal(row["Kin"]), axis=1)
    
    #Coluna dos 72 anjos - Números    
    cropData["Angel Number"] = cropData.apply(lambda row: AngelsNum(row["Month"],row["Day"]), axis=1 )
    
    #Coluna dos 72 anjos - Nomes    
    cropData["Angel Names"] = cropData.apply(lambda row: AngelsNam(row["Angel Number"]), axis=1 )
    
    #Coluna das 9 hierarquias angelicais
    cropData["Hierarchy"] = cropData.apply(lambda row: AngelsHierarchy(row["Angel Number"]),axis=1 )
    #######################################################
    
    #Tabela elementos kin    
    cropElements = cropData[["Kin","Element Kin","Stamp","Gate","Latitude","Longitude","Link","Image"]]
    
    #Tabela Fogo
    cropFireTrue = (cropElements["Element Kin"] == "Fire")
    cropFire = cropElements[cropFireTrue]
    
    #Tabela Ar
    cropAirTrue = (cropElements["Element Kin"] == "Air")
    cropAir = cropElements[cropAirTrue]
    
    #Tabela Água
    cropWaterTrue = (cropElements["Element Kin"] == "Water")
    cropWater = cropElements[cropWaterTrue]
    
    #Tabela Terra
    cropGroundTrue = (cropElements["Element Kin"] == "Ground")
    cropGround = cropElements[cropGroundTrue]
    
    #Tabela Portal
    cropGateTrue = (cropData["Gate"] == "Yes")
    cropGate = cropData[cropGateTrue]
    
    #Tabela Fogo
    cropFireGateTrue = (cropGate["Element Kin"] == "Fire")
    cropGateFire = cropGate[cropFireGateTrue]
    
    #Tabela Portal Ar
    cropAirGateTrue = (cropGate["Element Kin"] == "Air")
    cropGateAir = cropGate[cropAirGateTrue]
    
    #Tabela Portal Água
    cropWaterGateTrue = (cropGate["Element Kin"] == "Water")
    cropGateWater = cropGate[cropWaterGateTrue]
    
    #Tabela Portal Terra
    cropGroundGateTrue = (cropGate["Element Kin"] == "Ground")
    cropGateGround = cropGate[cropGroundGateTrue]
    
    
    
    
    
    #Tabela dos Serafins
    cropSerafinTrue = (cropData["Hierarchy"]=="Serafins")
    cropSerafin = cropData[cropSerafinTrue]
    
    #Tabela dos Cherubins
    cropCherubinTrue = (cropData["Hierarchy"]=="Cherubins")
    cropCherubin = cropData[cropCherubinTrue]
    
    #Tabela dos Ophanim
    cropOphanimTrue = (cropData["Hierarchy"]=="Ophanim")
    cropOphanim = cropData[cropOphanimTrue]

    #Tabela dos Dominions
    cropDominionTrue = (cropData["Hierarchy"]=="Dominions")
    cropDominion = cropData[cropDominionTrue]
    
    #Tabela dos Powers
    cropPowerTrue = (cropData["Hierarchy"]=="Powers")
    cropPower = cropData[cropPowerTrue]
    
    #Tabela dos Virtues
    cropVirtueTrue = (cropData["Hierarchy"]=="Virtues")
    cropVirtue = cropData[cropVirtueTrue]
    
    #Tabela dos Rulers
    cropRulerTrue = (cropData["Hierarchy"]=="Rulers")
    cropRuler = cropData[cropRulerTrue]
    
    #Tabela dos Archangels
    cropArchangelTrue = (cropData["Hierarchy"]=="Archangels")
    cropArchangel = cropData[cropArchangelTrue]
    
    #Tabela dos Angels
    cropAngelTrue = (cropData["Hierarchy"]=="Angels")
    cropAngel = cropData[cropAngelTrue]
            
    ######################################################################
    #Adicionando função de calor no mapa
    coordTotal = cropData[["Latitude","Longitude"]].values.tolist()
    HeatMap(coordTotal, radius=52).add_to(m)
      
    ########################################################################
       
    ############################################################
    #Localizações dos Crops no mapa  
     
    # All Crops
    loc=cropData['Locate']
    lat= cropData['Latitude']
    lon = cropData['Longitude']   
    
    for c, la, lo in zip(loc, lat, lon):
        folium.Circle([la,lo], tooltip=c,
                                     radius =33000, 
                                     color ="white",
                                     weight = 1,
                                     #fill_color="blue",
                                     fill_opacity = 0.1
                                     ).add_to(m) 
     
# Classificação Maia dos Crops
        
    latFire= cropFire['Latitude']
    lonFire = cropFire['Longitude'] 
    kinFire = cropFire["Kin"]    
    
    for c, la, lo in zip(kinFire, latFire, lonFire):
        folium.Circle([la,lo], tooltip=c,
                                     radius =33000, 
                                     color ="red",
                                     weight = 1,
                                     fill_color="red",
                                     fill_opacity = 0.4
                                     ).add_to(mElement)
    
    latAir= cropAir['Latitude']
    lonAir = cropAir['Longitude']
    kinAir = cropAir["Kin"]
    
    for c, la, lo in zip(kinAir, latAir, lonAir):
        folium.Circle([la,lo], tooltip=c,
                                     radius =33000, 
                                     color ="white",
                                     weight = 1,
                                     fill_color="white",
                                     fill_opacity = 0.3
                                     ).add_to(mElement)
    
    latWater= cropWater['Latitude']
    lonWater = cropWater['Longitude']
    kinWater = cropWater["Kin"]
    
    for c, la, lo in zip(kinWater, latWater, lonWater):
        folium.Circle([la,lo], tooltip=c,
                                     radius =33000, 
                                     color ="blue",
                                     weight = 1,
                                     fill_color="blue",
                                     fill_opacity = 0.2
                                     ).add_to(mElement)
    
    latGround= cropGround['Latitude']
    lonGround = cropGround['Longitude'] 
    kinGround = cropGround["Kin"]
    
    for c, la, lo in zip(kinGround, latGround, lonGround):
        folium.Circle([la,lo], tooltip=c,
                                     radius =33000, 
                                     color ="yellow",
                                     weight = 1,
                                     fill_color="yellow",
                                     fill_opacity = 0.1
                                     ).add_to(mElement) 
    
    # latGate= cropGate['Latitude']
    # lonGate = cropGate['Longitude'] 
    # kinGate = cropGate["Kin"]
    
    latGateFire= cropGateFire['Latitude']
    lonGateFire = cropGateFire['Longitude'] 
    kinGateFire = cropGateFire["Kin"]    
    
    for c, la, lo in zip(kinGateFire, latGateFire, lonGateFire):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="red",
                                     weight = 1,
                                     fill_color="red",
                                     fill_opacity = 0.4
                                     ).add_to(mPortal)
    
    latGateAir= cropGateAir['Latitude']
    lonGateAir = cropGateAir['Longitude']
    kinGateAir = cropGateAir["Kin"]
    
    for c, la, lo in zip(kinGateAir, latGateAir, lonGateAir):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="white",
                                     weight = 1,
                                     fill_color="white",
                                     fill_opacity = 0.3
                                     ).add_to(mPortal)
    
    latGateWater= cropGateWater['Latitude']
    lonGateWater = cropGateWater['Longitude']
    kinGateWater = cropGateWater["Kin"]
    
    for c, la, lo in zip(kinGateWater, latGateWater, lonGateWater):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="blue",
                                     weight = 1,
                                     fill_color="blue",
                                     fill_opacity = 0.2
                                     ).add_to(mPortal) 
    
    latGateGround= cropGateGround['Latitude']
    lonGateGround = cropGateGround['Longitude'] 
    kinGateGround = cropGateGround["Kin"]
    
    for c, la, lo in zip(kinGateGround, latGateGround, lonGateGround):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="yellow",
                                     weight = 1,
                                     fill_color="yellow",
                                     fill_opacity = 0.1
                                     ).add_to(mPortal)  
        
   #Classificação angelical dos crops
   
    latSeraphin= cropSerafin['Latitude']
    lonSeraphin = cropSerafin['Longitude'] 
    nameAngel = cropSerafin["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latSeraphin, lonSeraphin):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="white",
                                     weight = 1,
                                     fill_color="white",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels)  
    
    latCherubin= cropCherubin['Latitude']
    lonCherubin = cropCherubin['Longitude'] 
    nameAngel = cropCherubin["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latCherubin, lonCherubin):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="blue",
                                     weight = 1,
                                     fill_color="blue",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels)    
   
    latOphanim= cropOphanim['Latitude']
    lonOphanim = cropOphanim['Longitude'] 
    nameAngel = cropOphanim["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latOphanim, lonOphanim):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="red",
                                     weight = 1,
                                     fill_color="red",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels) 
        
    latDominion= cropDominion['Latitude']
    lonDominion = cropDominion['Longitude'] 
    nameAngel = cropDominion["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latDominion, lonDominion):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="yellow",
                                     weight = 1,
                                     fill_color="yellow",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels) 
        
    latPower= cropPower['Latitude']
    lonPower = cropPower['Longitude'] 
    nameAngel = cropPower["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latPower, lonPower):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="green",
                                     weight = 1,
                                     fill_color="green",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels) 
        
    latVirtue= cropVirtue['Latitude']
    lonVirtue = cropVirtue['Longitude'] 
    nameAngel = cropVirtue["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latVirtue, lonVirtue):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="pink",
                                     weight = 1,
                                     fill_color="pink",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels) 
        
    latRuler= cropRuler['Latitude']
    lonRuler = cropRuler['Longitude'] 
    nameAngel = cropRuler["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latRuler, lonRuler):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="purple",
                                     weight = 1,
                                     fill_color="purple",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels) 
        
    latArchangel= cropArchangel['Latitude']
    lonArchangel = cropArchangel['Longitude'] 
    nameAngel = cropArchangel["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latArchangel, lonArchangel):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="black",
                                     weight = 1,
                                     fill_color="black",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels)
    
    latAngel= cropAngel['Latitude']
    lonAngel = cropAngel['Longitude'] 
    nameAngel = cropAngel["Angel Names"]
    
    for c, la, lo in zip(nameAngel, latAngel, lonAngel):
        folium.Circle([la,lo], tooltip=c,
                                     radius =52000, 
                                     color ="grey",
                                     weight = 1,
                                     fill_color="grey",
                                     fill_opacity = 0.1
                                     ).add_to(mAngels)
        
    
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
    # Gráfico em Barra - Anjos por Ano     
    yearAngels = cropData[["Year","Hierarchy"]].value_counts().reset_index()
    yearAngelsBar = px.bar(yearAngels, 
                       x="Year",
                       y="count",
                       color="Hierarchy",
                       title="Anjos em cada ano")
    
    # Gráfico em Barra - Anjos por Mês     
    yearMonth = cropData[["Year","Month"]].value_counts().reset_index()
    yearMonthBar = px.bar(yearMonth, 
                       x="Year",
                       y="count",
                       color="Month",
                       title="Ano/Mês")
    #########################################################################
    #Quantidade de Crops    
    
    totalCrops = cropData.shape[0]   
    #Quantidade de Portais
    totalGate = cropGate.shape[0]      
    #Quantidade de Portais Fogo/Plasma
    totalGateFire = cropGateFire.shape[0]    
    #Quantidade de Portais Ar/Gás
    totalGateAir = cropGateAir.shape[0]    
    #Quantidade ee Portais Água/Líquido
    totalGateWater = cropGateWater.shape[0]    
    #Quantidade de Portais Terra/Sólido
    totalGateGround = cropGateGround.shape[0]
    #############################################################
    #Parâmetros do Site
    col1, col2, col3, col4, col5, col6 = st.columns(6)
        
    #Chamadas no Site
        
    #st.write(Kin(ano=anoA,mes=mesA,dia=diaA))
    
    #Mapas
    
    st.header("Mapa de calor com todos os círculos")
    folium_static(m) 
    yearCropsBar
    
    yearMonthBar   
    
    st.header("Classificação Angelical dos Crops no Mapa - Hierarquia")
    folium_static(mAngels)
    yearAngelsBar
    
    #folium_static(mPortalAngels)   
    #folium_static(mElement)   
    #folium_static(mPortal) 
       
      
    col1.metric(label="Total Crops", value=totalCrops)
    col2.metric(label="Total Gates", value=totalGate)
    col3.metric(label="Total Fire Gates", value=totalGateFire)
    col4.metric(label="Total Air Gates", value=totalGateAir)
    col5.metric(label="Total Water Gates", value=totalGateWater)
    col6.metric(label="Total Ground Gates", value=totalGateGround)
    #Gráfico em Pizza de Crops por País
    pieCountryCrops
    #Gráfico de Barras - Crops por Ano        
     
    
    
    #dataset   
    # cropSerafin
    # cropCherubin
    # cropOphanim
    # cropDominion
    # cropPower
    # cropVirtue
    # cropRuler
    # cropArchangel
    # cropAngel
    # cropGate
    cropData        
    ##################################################################
if __name__ == "__main__":
    main()
    