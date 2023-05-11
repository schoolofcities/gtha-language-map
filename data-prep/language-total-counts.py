import pandas as pd
import numpy as np

df = pd.read_csv("data/cd-totals.csv")

characteristic_ids = np.loadtxt("language-characteristic-ids.txt".format(""), unpack=True)

df = df[df['CHARACTERISTIC_ID'].isin(characteristic_ids)]

df = df[["CHARACTERISTIC_NAME", "C1_COUNT_TOTAL"]]

df = df.groupby(['CHARACTERISTIC_NAME'])['C1_COUNT_TOTAL'].sum().reset_index()

df.to_csv("langauge-totals-gtha.csv")

