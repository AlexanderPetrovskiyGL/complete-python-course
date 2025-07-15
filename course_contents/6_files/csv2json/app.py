import json
import csv

json_object: list[dict] = []

with open('csv_file.txt', 'r') as file:
    for row in csv.DictReader(file, fieldnames=['club', 'city', 'country']):
        json_object.append(row)

with open('json_file.txt', 'w') as file:
    json.dump(json_object, file)
