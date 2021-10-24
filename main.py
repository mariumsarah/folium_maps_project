import folium

def main():
    # look into more arguments in map function use dir(folium) or help(folium.Map)
    map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles = "Stamen Terrain")

    # Now let's add a marker
    map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a marker",icon=folium.Icon(color='green')))

    map.save("Map1.html")

if __name__ == "__main__":
    main()
