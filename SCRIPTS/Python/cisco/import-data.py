# Python script to import information from spreadsheet 

import csv 

source_file = "/home/roger/network-programmability/SCRIPTS/Python/cisco/router-details.csv"

with open(source_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)




