import json
import csv

data = {
    'name': 'Max',
    'age': 31,
    'gender': 'male'
}

with open ('example.json', 'w') as file:
    json.dump(data, file)

with open('example.json', 'r') as file:
    dataJson = json.load(file)
    print(dataJson)
    print(type(dataJson))

with open('example.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(dataJson.values())
