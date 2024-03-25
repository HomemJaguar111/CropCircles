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
    #Inserindo novas colunas na tabela
    
    #Coluna dos Kins Maya
    cropData["Kin"] = cropData.apply(lambda row: Kin(row["Year"], row["Month"], row["Day"]), axis=1)
        
    #Coluna dos Elementos Kin
    cropData["Element Kin"] = cropData.apply(lambda row: ElementKin(row["Kin"]), axis=1)
    
    #Coluna dos 72 anjos - Números    
    cropData["Angel Number"] = cropData.apply(lambda row: AngelsNum(row["Month"],row["Day"]), axis=1 )
    
    #Coluna dos 72 anjos - Nomes    
    cropData["Angel Names"] = cropData.apply(lambda row: AngelsNam(row["Angel Number"]), axis=1 )
    
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
