import pandas as pd
import zipfile
import numpy as np

import_zip = "data/98-401-X2021006_Ontario_eng_CSV.zip" 
import_csv = "98-401-X2021006_English_CSV_data_Ontario.csv" 
zf = zipfile.ZipFile(import_zip) 

# dauid geocodes

# create a list to hold each chunk of data
data_chunks = []

# iterate over the chunks and append them to the list
for df in pd.read_csv(zf.open(import_csv), dtype=str, encoding='latin1', chunksize=10000):

    #convert the df data types to numeric
    df["C1_COUNT_TOTAL"] = df["C1_COUNT_TOTAL"].astype(float)
    df["CHARACTERISTIC_ID"] = df["CHARACTERISTIC_ID"].astype(int)
    df["ALT_GEO_CODE"] = df["ALT_GEO_CODE"].astype(int)

    #limit df to containing only desired CHARACTERISTIC_ID's
    characteristic_ids = [] #input list of desired CHARACTERISTIC_ID's (can use the loadtxt function below, or any other function)
    characteristic_ids = np.loadtxt("language-characteristic-ids.txt".format(""), unpack=True)
    df = df[df['CHARACTERISTIC_ID'].isin(characteristic_ids)]

    #limit df to containing only desired ALT_GEO_CODE's
    alt_ids = [] #input list of desired ALT_GEO_CODE's (can use the loadtxt function below, or any other function)
    alt_ids= np.loadtxt("GTA ALT_GEO_CODE's.txt".format(""), unpack=True) 
    df = df[df['ALT_GEO_CODE'].isin(alt_ids)]

    #limit df to containing only the ALT_GEO_CODE, CHARACTERISTIC_NAME AND C1_COUNT_TOTAL columns
    df = df[["ALT_GEO_CODE","CHARACTERISTIC_NAME","C1_COUNT_TOTAL"]]

    #reformat df, using the ALT_GEO_CODE as the index and the CHARACTERISTIC_NAME's as the columns
    
    data_chunks.append(df)
 

# concatenate the list of data chunks into a single dataframe
df = pd.concat(data_chunks)

df = pd.pivot(df, index='ALT_GEO_CODE', columns='CHARACTERISTIC_NAME', values='C1_COUNT_TOTAL')

# print the dataframe
df.to_csv("da-languages-gtha-test.csv")