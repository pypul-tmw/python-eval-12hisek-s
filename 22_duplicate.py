import csv
with open("raw.csv","r") as f:
    reader = csv.DictReader(f)
    data = list(reader)


def remove_duplicates(data,column):
    seen = set()
    new_data = []

    for row in data:
        if row[column] not in seen:
            new_data.append(row)
            seen.add(row[column])
    return new_data

data = remove_duplicates(data,'Name')

with open('cleaned.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data:
        writer.writerow(row)