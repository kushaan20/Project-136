import pandas as pd
import csv

df = pd.read_csv('final.csv')
print(df.shape)

del df['hyperlink']
print(df.shape)

df.dropna()

del df['Luminosity (L☉)']

del df['Radius(RJ)']

del df['Mass(RJ)']

del df['Distance (ly)']

del df['']

del df['']

print(df.shape)
print(list(df))

df.to_csv('main.csv')

print(list(df))