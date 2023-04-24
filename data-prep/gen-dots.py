import pandas as pd
import numpy as np
from shapely.geometry import Point
import random
import geopandas as gpd

df = pd.read_csv("da-languages-gtha.csv")

language_keep_list=[]
language_delete_list=[]
for j in range(len(df.columns)): #loops through all columns of df
    count=0
    for i in range(len(df)): #loop through all rows of df
        if np.isnan(df.iloc[i, j])==False and df.iloc[i, j]>=10: #if the number of speakers for a given language in a given census tract is greater than 10, increase the "count" value by 1
            count=count+1
    if count<1: #if the total number of census tracts having more than 10 speakers is less than 10, add language to a "delete" list
        #print("deleted", df.columns[j]) #optionally, uncomment to see languages being deleted
        language_delete_list.append(df.columns[j])
    elif count>=1: #if the total number of census tracts having more than 10 speakers is greater than 10, add language to a "keep" list (and remove leading/trailing whitespace in its name)
        language_keep_list.append((df.columns[j]).strip()) 
        df = df.rename(columns={df.columns[j]: (df.columns[j]).strip() }) #rename df columns for kept languages to remove leading/trailing whitespace


#Assuming the "df" created in cell 2 contains ALL languages as its characteristics (either mother tongues, most spoken languages, etc),
#this cell creates a dataframe "df2" which limits the characteristics to a user-selected list of a desired few languages 
#and adds an "other" column to account for all languages NOT included in the user's selected list
#Note: user can first use the code in CELL 4 below to find list of languages with highest number of speakers

#loops through every language for every ALT_GEO_CODE in the dataframe "df" created in cell 2: if the language is NOT 
#part of a user-selected list, appends the number of people speaking that language to an "other" list
other_list_total=[]
for i in range(len(df)):
    other_list_total.append(0)
    for j in range(len(df.columns)):
        if df.columns[j] not in language_keep_list: #list of column names corresponding to desired languages (NOT to be placed in the "other" category)
            if np.isnan(df.iloc[i, j])==False:
                other_list_total[-1]=other_list_total[-1]+df.iloc[i, j]

#deletes columns corresponding to languages with no enough speakers
for val in language_delete_list:
    del df[val]
    
#creates a new dataframe "df2" which contains as columns only the languages in the user-selected list inputed above + an other category
df2 = df[language_keep_list]
df2.insert(len(language_keep_list), 'Other', other_list_total) 




# generate dots

def gen_dot(polygon, number):
    points = []    
    while len(points) < number:
        pnt = Point(random.uniform(polygon.bounds[0], polygon.bounds[2]), random.uniform(polygon.bounds[1], polygon.bounds[3]))
        if (polygon.contains(pnt)==True):
            points.append([round(pnt.x,5),round(pnt.y,5)])
    return points


gdf = gpd.read_file("gtha-da-2021-clipped.geojson")

dots = []

for index, row in df2.iterrows():

    dauid = str(int(row["ALT_GEO_CODE"]))
    print(dauid)

    geom = gdf[gdf['DAUID'] == dauid].geometry.values[0]
    
    for column in df2.columns.tolist()[1:]:
        if row[column] > 9:
            
            pt = gen_dot(geom, 1)
            dots.append([dauid, column, row[column], pt[0]])

    break

points = [Point(xy) for xy in [d[3] for d in dots]]
dots = gpd.GeoDataFrame(dots, columns=['d', 'l', 's', 'c'], geometry=points)

dots.crs = 'EPSG:4326'
dots = dots[['d','l','s','geometry']]

dots.to_file('gtha-da-2021-langauge-dots.geojson', driver='GeoJSON')
