import csv
import json5
csvfilepath = "data.csv"
jsonfilepath = 'data.json'

# read csv and add it to a dictionary
with open(csvfilepath) as csvfile:
    csvReader = csv.reader(csvfile)
    next(csvReader)
    data = []
    for csvRow in csvReader:
        data.append({"FileId": csvRow[0], "Number": csvRow[1], "ClassId": csvRow[2]})

# write data to a json file
with open(jsonfilepath, "w") as jsonfile:
    jsonfile.write(json5.dumps(data, indent=5))
