import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv',names=['word','bin'])

count = 1
minimum = 200
for  i in range(df.shape[0]):
    for j in range(i+1, df.shape[0]):
        hd =hamming(df.iloc[i,1],df.iloc[j,1])
        print(count, "(", df.iloc[i,0],df.iloc[j,0],")haming_distance: ",hd)
        count+= 1
        if minimum > hd:
            minimum = hd

print("min hamming distance", minimum)
