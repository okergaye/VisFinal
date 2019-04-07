# Import libraries
import pandas as pd
import folium
import folium.plugins
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
m = folium.plugins.DualMap(location=[37, -102], zoom_start=5)





# # Lets load the csv files:
# diseaseTypes = ['a3', 'a3', 'a25', 'i4', 'i4', 'i4', 'i4',
#                 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4']
# diseaseData = np.genfromtxt(
#     './measles_disease_data.csv', dtype=diseaseTypes, delimiter=',', names=True)
# countries = diseaseData['Country']

# for country in countries:
#     print(country)

# user_input = input("Type in a year")
# year = 0
# if user_input == "exit":
#     exit(0)
# else:
#     try:
#         year = int(user_input)
#     except:
#         print("Not a valid year")
#         exit(0)
# print(year)

worldmap = os.path.join('./', 'world.json')

# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
measles_disease_path = os.path.join(
    './', 'measles_disease_data.csv')
measles_disease_datam = pd.read_csv(measles_disease_path)

# Initialize the map:
disease_map = folium.Map(location=[37, -102], zoom_start=5)

measles_disease_bins = list(measles_disease_datam['2012'].quantile([0, 0.25, 0.5, 0.75, 1]))


# Add the color for the chloropleth:
m.m2.choropleth(
    geo_data=worldmap,
    name='choropleth',
    data=measles_disease_datam,
    columns=['ISO3', '2012'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Measle Occurence \# of people',
    bins=measles_disease_bins
)
folium.LayerControl().add_to(m.m2)

# folium.LayerControl().add_to(disease_map)


measles_vaccine_path = os.path.join('./', 'measles_vaccine_data.csv')
measles_vaccine_datam = pd.read_csv(measles_vaccine_path, encoding='iso-8859-1')


measles_vaccine_bins = list(measles_vaccine_datam['2012'].quantile([0, 0.25, 0.5, 0.75, 1]))

m.m1.choropleth(
    geo_data=worldmap,
    name='choropleth',
    data=measles_vaccine_datam,
    columns=['Country Code', '2012'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Percent of Country Vaccinated',
    # bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101]
    bins=measles_vaccine_bins
)
folium.LayerControl().add_to(m.m1)

# folium.LayerControl().add_to(disease_map)

# Save to html
disease_map.save('disease_map.html')
# Save to html
m.save('test.html')