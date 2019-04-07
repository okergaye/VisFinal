# Import libraries
import pandas as pd
import folium
import folium.plugins
from folium.plugins import TimeSliderChoropleth
from folium.features import Choropleth

import os
import numpy as np

# Initialize the map:
m = folium.plugins.DualMap(location=[37, -102], zoom_start=5)

worldmap = os.path.join('./', 'world.json')

# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
measles_disease_path = os.path.join(
    './', 'measles_disease_data.csv')
measles_disease_datam = pd.read_csv(measles_disease_path)


# probably start loop here !!!!!!!!!!!!!!!!!!!!!!
for x in range(2011, 2020):
    year = "" + x.__str__()
    # print(year)
    measles_disease_bins = list(
        measles_disease_datam[year].quantile([0, 0.25, 0.5, 0.75, 1]))
    Choropleth(
        geo_data=worldmap,
        name=year,
        data=measles_disease_datam,
        columns=['ISO3', year],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        # legend_name='Measle Occurence \# of people',
        bins=measles_disease_bins
    ).add_to(m.m2)


measles_vaccine_path = os.path.join('./', 'measles_vaccine_data.csv')
measles_vaccine_datam = pd.read_csv(
    measles_vaccine_path, encoding='iso-8859-1')


for x in range(1980, 2018):
    year = "" + x.__str__()
    measles_vaccine_bins = list(
        measles_vaccine_datam[year].quantile([0, 0.25, 0.5, 0.75, 1]))
    Choropleth(
        geo_data=worldmap,
        name=year,
        data=measles_vaccine_datam,
        columns=['Country Code', year],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Percent of Country Vaccinated',
        bins=measles_vaccine_bins
    ).add_to(m.m1)


folium.LayerControl().add_to(m)

# Save to html
m.save('Measles Data.html')
