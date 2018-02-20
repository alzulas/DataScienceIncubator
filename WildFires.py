#I have failed to make either of my code attempts work. I have no graphs to show. I've run out of time. 



#import sqlite3
#import numpy as np
#import pandas as pd
#import plotly.offline as py
#import plotly.graph_objs as go

import pandas as pd 
import matplotlib.pyplot as plt
import sqlite3


# read lat/lng data into panda dataframe
conn = sqlite3.connect('FPA_FOD_20170508.sqlite')

#df = pd.read_sql_query("SELECT latitude, longitude FROM fires;", conn)

#df_year = pd.read_sql_query("SELECT 'FIRE_YEAR' From fires", conn)
#df.head()

df = pd.read_sql_query("SELECT * From Fires", conn)
df.head()

# Create new DataFrame Populated with Relevant Data
df_year = df[['FIRE_YEAR']]
df_state = df[['STATE']]

def barGraphOfInstancesPerYear():
	df_year['FIRE_YEAR'].value_counts(sort=False).plot(kind="bar", color='b', figsize=(8,5))
	plt.title('Number of Wildfires between 1992 and 2015')
	plt.xlabel('Year')
	plt.ylabel('Number of Fires')
	plt.show()

def barGraphOfInstancesPerState():
	df_state['STATE'].value_counts(sort=True).plot(kind="bar", color='b', figsize=(8,5))
	plt.title('Number of Wildfires by State')
	plt.xlabel('State')
	plt.ylabel('Number of Fires')
	plt.show()

def histGraphOfSizeOfFire():
	df_size = df[['FIRE_SIZE']]
	df_size = df_size.sort_values("FIRE_SIZE")

	# Determine mean value
	df_size["FIRE_SIZE"].mean()

	# Histogram plot of all instances 
	df_size.plot(kind="hist")
	plt.title('How many fires by each size')
	plt.xlabel('Size in Acres')
	plt.ylabel('Number of Fires')
	plt.show()

def barGraphOfSizeByClass():
	# Bar plot with FIRE_SIZE_CLASS grouping
	df_size_class = df[['FIRE_SIZE_CLASS']]
	df_size_class.groupby('FIRE_SIZE_CLASS').size().plot(kind='bar', color='r', figsize=(8,5))
	plt.title('How many fires by class')
	plt.xlabel('Fire Classification')
	plt.ylabel('Number of Fires')
	plt.show()

#comment out all but the graph you want to see
#barGraphOfInstancesPerYear()
barGraphOfInstancesPerState()
#histGraphOfSizeOfFire()
#barGraphOfSizeByClass()

#fires = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
# Create new DataFrame Populated with Relevant Data
#df_year = df[['FIRE_YEAR']]
#for year in df_year:{
#	print (year)
	#year = year - 1992
	#fires[year] = fires[year] + 1
#}

#1992-2015 
#fires = df_year['FIRE_YEAR'].value_counts(sort=False).plot(kind="line",marker='o', figsize=(8,5))



#lats = df['LATITUDE']
#lons = df['LONGITUDE']



# data = [go.Bar(
#             x=[fires],
#             y=[1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
#     )]

# py.iplot(data, filename='basic-bar')


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
