from flask import Flask, jsonify, request
from data import data
import pandas as pd
import csv

planet_data_rows = []
final_planet_list = []
final_dict = []
rows = []

with open('final.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        rows.append(row)

for planet_data in planet_data_rows:
  temp_dict = {
                  "name": planet_data[1],
                  "distance_from_earth": planet_data[2],
                  "planet_mass": planet_data[3],
                  "planet_type": planet_data[6],
                  "planet_radius": planet_data[7],
                  "distance_from_their_sun": planet_data[8],
                  "orbital_period": planet_data[9],
                  "gravity": planet_data[20],
                  "orbital_speed": planet_data[21]
              }
  temp_dict["specifications"] = final_dict[planet_data[1]]
  final_planet_list.append(temp_dict)

print(final_planet_list)

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()