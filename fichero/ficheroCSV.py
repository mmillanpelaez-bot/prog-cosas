import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # encabezado
    writer.writerow(['Name', 'Age', 'Gender'])
    # datos
    writer.writerow(['Manolo', '67', 'Undefined'])
    writer.writerow(['Garminedes', 'Unknown', 'Female'])

with open('example.csv', 'r') as file:
    writer = csv.writer(file)

    writer.writerow(['Name', 'Age', 'Gender'])

    writer.writerow(['Manolo', '67', 'Undefined'])
    writer.writerow(['Garminedes', 'Unknown', 'Female'])

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
