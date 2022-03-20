import csv

data = []

with open("dataset2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
stars_data = data[1:]

for data_point in stars_data:
    data_point[2] = data_point[2].lower()

stars_data.sort(key=lambda stars_data: stars_data[2])


with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)