import csv
import pandas as pd
import matplotlib as mp
import plotly
import plotly_express as px

rows = []
stars_distance = []

with open('final.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        rows.append(row)

temp_suitable_planets = list(f)
for planet_data in temp_suitable_planets:
  if planet_data[8].lower() == "unknown":
    f.remove(planet_data)

for planet_data in f:
  if planet_data[9].split(" ")[1].lower() == "days":
    planet_data[9] = float(planet_data[9].split(" ")[0]) #Days
  else:
    planet_data[9] = float(planet_data[9].split(" ")[0])*365 #Years
  planet_data[8] = float(planet_data[8].split(" ")[0])

orbital_radiuses = []
orbital_periods = []
for planet_data in f:
  orbital_radiuses.append(planet_data[8])
  orbital_periods.append(planet_data[9])

fig = px.scatter(x=orbital_radiuses, y=orbital_periods)
fig.show()

planet_masses = []
planet_radiuses = []
planet_types = []
for planet_data in f:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses, y=planet_masses, color=planet_types)
fig.show()

for planet_data in f:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])

fig = px.scatter(x = planet_radiuses, y = planet_masses)
fig.show()
for planet_data in f:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  rows.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(f):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()