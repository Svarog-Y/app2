import os
import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")

html = """<h4> Volcano information:</h4>
Name: <b><a href="https://www.google.com/search?q=%s,+%s+Volcano+site=www.wikipedia.org&btnI=Search" target="_blank">%s</a></b><br>
Height: <i> %s m</i>
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for ind in df.index:
    iframe = folium.IFrame(
        html=html % (
            df['NAME'][ind], 
            df['LOCATION'][ind][3:], 
            df['NAME'][ind], 
            str(df['ELEV'][ind])
            ),
        width=250, 
        height=100
        )
    fg.add_child(folium.CircleMarker(
        location=[df['LAT'][ind], df['LON'][ind]], 
        radius = 8,
        opacity = 0.8,
        popup=folium.Popup(iframe),
        tooltip=df['NAME'][ind],
        color=color_producer(df['ELEV'][ind]),
        fill=True,
        fillColor=color_producer(df['ELEV'][ind]),
        fill_opacity=0.5
        ))

map.add_child(fg)
map.save(os.getcwd() + "\\Map2.html")