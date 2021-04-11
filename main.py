import csv
from collections import defaultdict

with open('tableDownload.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = defaultdict(float)
    first = 1
    for row in csv_reader:
        if first:
            first = 0
            continue
        sum = data[row[1]] + float(row[4])
        data[row[1]] = sum
    for coin in data:
        print(f"You have earned {data[coin]} in {coin}")
