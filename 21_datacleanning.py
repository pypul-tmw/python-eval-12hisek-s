import csv
with open("raw.csv","r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
    print(data)