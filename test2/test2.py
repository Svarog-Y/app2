import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")

html = """<h4> Volcano information:</h4>
Name: <b><a href="https://www.google.com/search?q=%s,+%s+Volcano+site=www.wikipedia.org&btnI=Search" target="_blank">%s</a></b><br>
Height: <i> %s m</i>
"""
#html = "<b>" + df['NAME'][ind] + "</b>" + ", <i>Elevation: " + str(df['ELEV'][ind]) + " m</i>"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for ind in df.index:
    iframe = folium.IFrame(html=html % (df['NAME'][ind], df['LOCATION'][ind][3:], df['NAME'][ind], str(df['ELEV'][ind])), width=250, height=100)
    fg.add_child(folium.Marker(
        location=[df['LAT'][ind], df['LON'][ind]], 
        popup=folium.Popup(iframe),
        icon=folium.Icon(color='red')
        ))

map.add_child(fg)
map.save("test2\\Map2.html")