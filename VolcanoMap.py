import folium
import pandas as pd

map = folium.Map(location=[41, -111], zoom_start=6, tiles='Stamen Terrain')

data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev_f = list(data['ELEV']*3.281)
name = list(data['NAME'])

def determineColor(elev):
   if elev < 4000:
      color = 'lightgreen'
   elif elev < 8000:
      color = 'green'
   else:
      color = 'cadetblue'

   return color

fg = folium.FeatureGroup(name='My Map')

for lt, ln, el, na in zip(lat, lon, elev_f, name):
   fg.add_child(folium.Marker(location=[lt, ln], popup=na+" "+str(round(el))+' f', icon=folium.Icon(color=determineColor(el), icon='flag')))

map.add_child(fg)

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:( {'fillColor':'yellow'} ))) # Change the polygons' colors to yellow.

map.save("Map1.html")
