import plotly.express as px

rows = []

planet_masses = []
planet_radiuses = []
planet_data_rows = rows[1:]
planet_gravity = []
planet_names = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

for planet_data in planet_data_rows:
  planet_masses.append(planet_data[6])
  planet_radiuses.append(planet_data[7])

fig = px.scatter(x = planet_radiuses, y = planet_masses)
fig.show()

fig2 = px.scatter(x = planet_gravity, y = planet_masses)
fig2.show()