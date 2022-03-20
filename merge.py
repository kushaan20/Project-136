import csv

dataset1 = []
dataset2 = []

with open('dataset1.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open('dataset_2_sorted.csv','r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

headers1 = dataset1[0]
dwarf_data = dataset2[1:]
headers2 = dataset2[0]
bright_data = dataset2[1:]

headers = headers1 + headers2

planet_data = []

for index, data_row in enumerate(dwarf_data):
    planet_data.append(dwarf_data[index]+bright_data[index])

with open('final.csv','a+') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)