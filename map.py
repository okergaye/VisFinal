# Import libraries
import pandas as pd
import folium
import os
import numpy as np

# Load the shape of the zone (US states)
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it
world_geo = os.path.join('./', 'world.json')

# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
state_unemployment = os.path.join(
    './', 'measles_disease_data.csv')
state_data = pd.read_csv(state_unemployment)

# Initialize the map:
m = folium.Map(location=[37, -102], zoom_start=5)

# Add the color for the chloropleth:
m.choropleth(
    geo_data=world_geo,
    name='choropleth',
    data=state_data,
    columns=['Country', 'January'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
)
folium.LayerControl().add_to(m)

# Save to html
m.save('testt.html')
m.save('test.html')


# Lets load the csv files:
diseaseTypes = ['a3', 'a3', 'a25', 'i4', 'i4', 'i4', 'i4',
                'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4']
diseaseData = np.genfromtxt(
    './measles_disease_data.csv', dtype=diseaseTypes, delimiter=',', names=True)
countries = diseaseData['Country']

# for country in countries:
#     print(country)

user_input = input("Type in a year")
year = 0
if user_input == "exit":
    exit(0)
else:
    try:
        year = int(user_input)
    except:
        print("Not a valid year")
        exit(0)
print(year)

worldmap = os.path.join('./', 'world.json')

# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
measles_disease_path = os.path.join(
    './', 'measles_disease_data.csv')
measles_disease_datam = pd.read_csv(measles_disease_path)

# Initialize the map:
disease_map = folium.Map(location=[37, -102], zoom_start=5)

# Add the color for the chloropleth:
disease_map.choropleth(
    geo_data=worldmap,
    name='choropleth',
    data=measles_disease_datam,
    columns=['ISO3', 'Total'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Measle Occurence \# of people',
    bins = [0, 10, 50, 100, 150, 200, 300, 3000, 50000]
)
folium.LayerControl().add_to(disease_map)

measles_vaccine_path = os.path.join('./', 'measles_vaccine_data.csv')
measles_vaccine_datam = pd.read_csv(measles_vaccine_path, encoding='iso-8859-1')

disease_map.choropleth(
    geo_data=worldmap,
    name='choropleth',
    data=measles_vaccine_datam,
    columns=['Country Code', '1980'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Measle Occurence \# of people',
    bins=[0, 10, 50, 100, 150, 200, 300, 3000, 50000]
)
folium.LayerControl().add_to(disease_map)

# Save to html
disease_map.save('disease_map.html')