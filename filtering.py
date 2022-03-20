import csv
import pandas as pd
import matplotlib as mp

rows = []

stars_distance = []
features_list = []

with open('final.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        rows.append(row)

for stars_data in f:
    if stars_distance<=100:
        features_list.append(stars_data)

for index, planet_data in enumerate(stars_data):
      features_list = []
      gravity = (float(planet_data[3])*5.972e+24)/(float(planet_data[7])*float(planet_data[7])*6371000*6371000)*6.674e-11
      try:
        if gravity<100:
            features_list.append('gravity')
      except:pass

print(features_list)