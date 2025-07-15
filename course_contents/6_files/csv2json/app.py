import json

with open('csv_file.txt', 'r') as file:
    file_records = [line.strip() for line in file.readlines()]

json_object: list[dict] = []

for record in file_records:
    club_value, city_value, country_value  = record.split(',')
    json_object.append({'club': club_value, 'city': city_value, 'country': country_value})

with open('json_file.txt', 'w') as file:
    json.dump(json_object, file)
