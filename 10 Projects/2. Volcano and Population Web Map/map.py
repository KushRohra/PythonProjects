import folium
import pandas

# Load data from files
data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")


# to get dynamic color based on elevation
def getColor(el):
    if el >= 3000:
        return 'red'
    elif el >= 2000:
        return 'orange'
    return 'green'


# Feature group for volcanoes
fgv = folium.FeatureGroup(name="My Map")

# Add points on the Feature Group
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(str(el) + "m", parse_html=True),
                                      fill_color=getColor(el), color='grey', fill_opacity=0.7))

# Feature group for population
fgp = folium.FeatureGroup(name="Population")

# Add geo data onto another layer of the map
# Using style function adding background color to polygon depending on the population of the region
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties'][
                                                                                   'POP2005'] < 10000000 else 'orange' if 10000000 <=
                                                                                                                          x[
                                                                                                                              'properties'][
                                                                                                                              'POP2005'] < 20000000 else 'red'}))

# Add the feature group(s) to map
map.add_child(fgv)
map.add_child(fgp)

# Using layer control we can switch between different layers of map
map.add_child(folium.LayerControl())

map.save("Map.html")
