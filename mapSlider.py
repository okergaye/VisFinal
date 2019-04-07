# Import libraries
import pandas as pd
import folium
import folium.plugins
from folium.plugins import TimeSliderChoropleth
from folium.features import Choropleth
import json
from branca.colormap import linear

import os
import numpy as np


# Initialize the map:
m = folium.plugins.DualMap(location=[37, -102], zoom_start=5)

worldmap = os.path.join('./', 'world.json')

measles_disease_path = os.path.join(
    './', 'measles_disease_data.csv')
measles_disease_datam = pd.read_csv(measles_disease_path)

# Initialize the map:
disease_map = folium.Map(location=[37, -102], zoom_start=5)

measles_disease_bins = list(
    measles_disease_datam['2012'].quantile([0, 0.25, 0.5, 0.75, 1]))


n_periods = 9
j = json.load(open('world.json', 'r'))
print(j["features"][1]['id'])
styledata = {}

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

for x in range(0, len(j["features"])):
    code = j["features"][x]['id']
    print(code)
    df = pd.DataFrame(
        {'color': np.random.normal(size=n_periods),
         'opacity': np.random.normal(size=n_periods)},
        index=year
    )
    df = df.cumsum()
    # df.sample(n_sample, replace=False).sort_index()
    df.sort_index()
    styledata[code] = df

print(styledata.items())
max_color, min_color, max_opacity, min_opacity = 0, 0, 0, 0

for code, data in styledata.items():
    max_color = max(max_color, data['color'].max())
    min_color = min(max_color, data['color'].min())
    max_opacity = max(max_color, data['opacity'].max())
    max_opacity = min(max_color, data['opacity'].max())


cmap = linear.PuRd_09.scale(min_color, max_color)


def norm(x):
    return (x - x.min()) / (x.max() - x.min())


for country, data in styledata.items():
    data['color'] = data['color'].apply(cmap)
    data['opacity'] = norm(data['opacity'])


styledict = {
    str(code): data.to_dict(orient='index') for
    code, data in styledata.items()
}

# Add the color for the chloropleth:
TimeSliderChoropleth(
    data=worldmap,
    styledict=styledict,
    name='monkey booze',
    # data=measles_disease_datam,
    # columns=['ISO3', '2012'],
    # key_on='feature.id',

).add_to(m.m2)
folium.LayerControl().add_to(m.m2)

# folium.LayerControl().add_to(disease_map)


measles_vaccine_path = os.path.join('./', 'measles_vaccine_data.csv')
measles_vaccine_datam = pd.read_csv(
    measles_vaccine_path, encoding='iso-8859-1')


measles_vaccine_bins = list(
    measles_vaccine_datam['2012'].quantile([0, 0.25, 0.5, 0.75, 1]))

Choropleth(
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
).add_to(m.m1)
folium.LayerControl().add_to(m.m1)

# folium.LayerControl().add_to(disease_map)

# Save to html
disease_map.save('disease_map.html')
# Save to html
m.save('slider.html')
