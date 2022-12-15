import pandas as pd
import zipfile

zip2021 = "sc/98-401-X2021007_eng_CSV.zip"
file2021 = "98-401-X2021007_English_CSV_data.csv"

zf = zipfile.ZipFile(zip2021) 
df = pd.read_csv(zf.open(file2021), dtype = str, encoding='latin1')

df["C1_COUNT_TOTAL"] = df["C1_COUNT_TOTAL"].astype(float)
df["CHARACTERISTIC_ID"] = df["CHARACTERISTIC_ID"].astype(int)

variable_ids = [1,2,3,4,5,50,56,57,113,115,128,130,199,201,212,214,229,230,238,239,331]

df = df[df['CHARACTERISTIC_ID'].isin(variable_ids)]

df = df[["ALT_GEO_CODE","CHARACTERISTIC_NAME","C1_COUNT_TOTAL"]]

df = pd.pivot(df, index='ALT_GEO_CODE', columns='CHARACTERISTIC_NAME', values='C1_COUNT_TOTAL')

df.to_csv("sc/clean2021.csv")