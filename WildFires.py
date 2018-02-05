import sqlite3
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


# read lat/lng data into panda dataframe
conn = sqlite3.connect('/Users/amandazulas/Downloads/RDS-2013-0009.4_SQLite/Data/FPA_FOD_20170508.sqlite')

#df = pd.read_sql_query("SELECT latitude, longitude FROM fires;", conn)

df_year = pd.read_sql_query("SELECT 'FIRE_YEAR' From fires", conn)
#df.head()

fires = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
# Create new DataFrame Populated with Relevant Data
#df_year = df[['FIRE_YEAR']]
for year in df_year:{
	print (year)
	#year = year - 1992
	#fires[year] = fires[year] + 1
}

#1992-2015 
#fires = df_year['FIRE_YEAR'].value_counts(sort=False).plot(kind="line",marker='o', figsize=(8,5))



#lats = df['LATITUDE']
#lons = df['LONGITUDE']



data = [go.Bar(
            x=[fires],
            y=[1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
    )]

py.iplot(data, filename='basic-bar')


# df.head()

# df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'
# limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
# colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]
# cities = []
# scale = 5000

# for i in range(len(limits)):
#     lim = limits[i]
#     df_sub = df[lim[0]:lim[1]]
#     city = dict(
#         type = 'scattergeo',
#         locationmode = 'USA-states',
#         lon = df_sub['lon'],
#         lat = df_sub['lat'],
#         text = df_sub['text'],
#         marker = dict(
#             size = df_sub['pop']/scale,
#             color = colors[i],
#             line = dict(width=0.5, color='rgb(40,40,40)'),
#             sizemode = 'area'
#         ),
#         name = '{0} - {1}'.format(lim[0],lim[1]) )
#     cities.append(city)

# layout = dict(
#         title = '2014 US city populations<br>(Click legend to toggle traces)',
#         showlegend = True,
#         geo = dict(
#             scope='usa',
#             projection=dict( type='albers usa' ),
#             showland = True,
#             landcolor = 'rgb(217, 217, 217)',
#             subunitwidth=1,
#             countrywidth=1,
#             subunitcolor="rgb(255, 255, 255)",
#             countrycolor="rgb(255, 255, 255)"
#         ),
#     )

# fig = dict( data=cities, layout=layout )
# py.iplot( fig, validate=False, filename='d3-bubble-map-populations' )
