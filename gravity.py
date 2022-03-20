import csv 

rows = []

with open('final.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]

print(headers)
print(planet_data_rows[0])

headers[0] = 'row_num'

temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass = planet_data[6]
    planet_mass_value = planet_mass.split(' ')[0]
    planet_mass_value = float(planet_mass_value)*1.989e+30
    planet_data[6] = planet_mass_value

    planet_radius = planet_data[7]

    planet_radius_value = planet_radius.split(' ')[0]
    planet_radius_value = float(planet_radius_value)*6.957e+8
    planet_data[7] = planet_radius_value

print(len(planet_data_rows))

temp_planet_data_rows = list(planet_data_rows)

planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)