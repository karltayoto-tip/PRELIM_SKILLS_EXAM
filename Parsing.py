import json
import csv

with open('covid_cases.json','r') as json_cases:
    cov = json.load(json_cases)

covid_info = cov['records']
covid_cases = open('covid_cases.csv','w')

csv_writer = csv.writer(covid_cases)

count = 0

for i in covid_cases:
    if count == 0:
        header = i.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(i.values())

covid_cases.close()