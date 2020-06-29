import folium
import pandas as pd

# as coordenadas do mapa aqui é do Brasil
m = folium.Map([-15.77972, -47.92972], zoom_start=4)

#ler os um arquivo em json
arq_json = 'Brasil.json'
#ler dados em csv
dados = pd.read_csv('Indicadores_de_Qualidade_de_Água_2001_a_2014__Média_do_Último_Ano_da_Série_de_Fósforo_Total.csv',sep=';')

#puxa os dados do json e csv dentro do mapa e da um formato
folium.Choropleth(
    geo_data=arq_json,
    data = dados,
    columns=['UF','NU1FOSFORO','ME1FOSFORO','MI1FOSFORO','MA1FOSFORO','SD1FOSFORO','LATITUDE','LONGITUDE'],
    key_on=['feature.properties.UF'],
    fill_opacity=0.3,
    line_weight=2,
).add_to(m)

#cria o map no html
m.save('mapa.html')