import pandas as pd
import numpy as np
from shapely.geometry import Point
import random
import geopandas

df = pd.read_csv("da-languages-gtha-test.csv")

language_keep_list=[]
language_delete_list=[]
for j in range(len(df.columns)): #loops through all columns of df
    count=0
    for i in range(len(df)): #loop through all rows of df
        if np.isnan(df.iloc[i, j])==False and df.iloc[i, j]>=10: #if the number of speakers for a given language in a given census tract is greater than 10, increase the "count" value by 1
            count=count+1
    if count<10: #if the total number of census tracts having more than 10 speakers is less than 10, add language to a "delete" list
        #print("deleted", df.columns[j]) #optionally, uncomment to see languages being deleted
        language_delete_list.append(df.columns[j])
    elif count>=10: #if the total number of census tracts having more than 10 speakers is greater than 10, add language to a "keep" list (and remove leading/trailing whitespace in its name)
        language_keep_list.append((df.columns[j]).strip()) 
        df = df.rename(columns={df.columns[j]: (df.columns[j]).strip() }) #rename df columns for kept languages to remove leading/trailing whitespace


print(language_keep_list)
print(language_delete_list)


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


print(df2)


#defines function which creates a user-selected "number" of random points in each polygon region for each desired language 
def gen_dot(polygon, number):
    points = []    
    while len(points) < number:
        pnt = Point(random.uniform(polygon.bounds[0], polygon.bounds[2]), random.uniform(polygon.bounds[1], polygon.bounds[3]))
        if (polygon.contains(pnt)==True):
            points.append([pnt.x,pnt.y])
    return points


for index, row in df2.iterrows():
    print(row["ALT_GEO_CODE"])
    break



# #This cell creates randomly placed points in the polygon regions (corresponding to the ALT_GEO_CODEs) for each language which has more than 10 speakers

# #reads-in shapefile with desired polygons in which to generate the random points
# shapefile = geopandas.read_file("final_tracts.shp")

# #specifies the coordinate reference system of the shapefile
# # shapefile.crs=

# #initializes empty lists
# dauid_list=[]
# x_list=[]
# y_list=[]
# language_list=[]
# speaker_no_list=[]

# #loops through all polygons and all languages; creates 1 randomly placed point in each polygon for each language which has more than 10 speakers in that given polygon
# #saves the ALT_GEO_CODEs and coordinates of the randomly generated points, as well as their correponding languages and number of speakers, in separate lists
# for alt_code in list(df2.index.values): #input df or df2, depending on whether interested in all languages present in df, or in the user-selected languages + other category present in df2
#     for col in list(df2.columns.values): #input df or df2
#         if df2.loc[alt_code, col]>=10: #input df or df2; input desired threshold number of speakers for the languages above which a point will be generated for the latter
#             dauid_list.append(alt_code)
#             point=gen_dot(shapefile.iloc[shapefile[shapefile['DAUID'] == str(alt_code)].index.to_numpy()[0], 4], 1)[0] #modify indicies according to shapefile
#             x_list.append(point[0])
#             y_list.append(point[1])
#             language_list.append(col)
#             speaker_no_list.append(df2.loc[alt_code, col]) #input df or df2

#     break

# #creates a dataframe of the ALT_GEO_CODES, the coordinates of the random points placed within the polygons corresponding to them, the languages corresponding to the random points, and the latters' respective number of speakers
# dict={"DAUID": dauid_list, "x": x_list, "y": y_list, "Language": language_list, "Speaker_No": speaker_no_list}
# rand_points = pd.DataFrame(dict)


# #transforms the dataframe into a geodataframe using geopandas
# gdf = geopandas.GeoDataFrame(
#     rand_points, geometry=geopandas.points_from_xy(rand_points.x, rand_points.y))

# #optionally,  uncomment the lines below to print "gdf" and save it as a geojson file
# print(gdf)
# #gdf.to_file("", driver='GeoJSON')