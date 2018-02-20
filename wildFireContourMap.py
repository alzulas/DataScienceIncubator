import sqlite3
import pandas as pd
import numpy as np
import colorcet as cc
from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LogColorMapper

cnx = sqlite3.connect('FPA_FOD_20170508.sqlite')
df = pd.read_sql_query("SELECT LATITUDE, LONGITUDE, FIRE_SIZE, STATE, FROM fires", cnx)
df.head(5)

pd.options.mode.chained_assignment = None

data = df.loc[(df.loc[:,'STATE']!='AK') & (df.loc[:,'STATE']!='HI') & (df.loc[:,'STATE']!='PR')]

data.loc[:,'LATITUDE'] = ((data.loc[:,'LATITUDE']*10).apply(np.floor))/10
data.loc[:,'LONGITUDE'] = ((data.loc[:,'LONGITUDE']*10).apply(np.floor))/10
data.loc[:,'LL_COMBO'] = data.loc[:,'LATITUDE'].map(str) + '-' + data.loc[:,'LONGITUDE'].map(str)
LLData = data.groupby(['LL_COMBO', 'LATITUDE', 'LONGITUDE'])
print(LLData)

#This function plots the number of wildfires in the US by lat/lon
#lighter colors are more wildfires
def plotNumberOfWildFires():
	numWF = LLData['FIRE_SIZE'].agg(['count']).reset_index()
	numWF.head(5)

	source = ColumnDataSource(numWF)
	plotNum = figure(title="Number of overall wildfires from 1992 to 2015 ",
	           toolbar_location="below", plot_width=1400, plot_height=900)
	plotNum.background_fill_color = "black"
	plotNum.grid.grid_line_color = None
	plotNum.axis.visible = False
	colors = LogColorMapper(palette="Viridis256")
	glyph = plotNum.circle('LONGITUDE', 'LATITUDE', source=source,
	          color={'field': 'count', 'transform' : colors},
	          size=1.5)
	show(plotNum)


#This function plots the number of wildfires in the US by lat/lon
#lighters colors are larger fires
def plotSizeOfWildFires():
	sizeWF = LLData['FIRE_SIZE'].agg(['mean']).reset_index()
	sizeWF.head(5)

	source = ColumnDataSource(sizeWF)
	plotSize = figure(title="Mean size of wildfires in acres from 1992 to 2015",
	           toolbar_location="below", plot_width=1400, plot_height=900)
	plotSize.background_fill_color = "black"
	plotSize.grid.grid_line_color = None
	plotSize.axis.visible = False
	colors = LogColorMapper(palette="Viridis256")
	glyph = plotSize.circle('LONGITUDE', 'LATITUDE', source=source,
	          color={'field': 'mean', 'transform' : colors},
	          size=1.5)
	show(plotSize)



#Comment out the one you don't want to plot right now.
#plotNumberOfWildFires()
plotSizeOfWildFires()