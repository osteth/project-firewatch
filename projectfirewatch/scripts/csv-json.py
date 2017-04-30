import csv
import json

def convert():
    csvfile = open('MODIS_C6_Global_24h.csv', 'r')
    jsonfile = open('MODIS_C6_Global_24h.json', 'w')

    reader = csv.DictReader( csvfile)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

if __name__ == '__main__':
    convert()
