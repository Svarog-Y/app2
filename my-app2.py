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
vlc = folium.FeatureGroup(name="Volcanoes")
pop = folium.FeatureGroup(name="Population")

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
    vlc.add_child(folium.Circle(
        location=[df['LAT'][ind], df['LON'][ind]], 
        radius = 2000,
        opacity = 0.8,
        popup=folium.Popup(iframe),
        tooltip=df['NAME'][ind],
        color=color_producer(df['ELEV'][ind]),
        fill=True,
        fillColor=color_producer(df['ELEV'][ind]),
        fill_opacity=0.5
        ))

population = open("world.json", 'r', encoding='utf-8-sig').read()
pop_data = pandas.read_json(population, lines=True)

pop.add_child(
    folium.GeoJson(
        data= population, #(open("world.json", 'r', encoding='utf-8-sig').read()),
        name='Population',
        style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 100000000 else 'red'}
        )
    )

map.add_child(vlc)
map.add_child(pop)
map.add_child(folium.LayerControl())
map.save("Map.html")