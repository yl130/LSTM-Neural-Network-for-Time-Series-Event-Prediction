import csv
import sys
from imp import reload
reload(sys)
import importlib
importlib.reload(sys)



ip_list = []
result = {}

with open('../data/file.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    ip_list.append(row['NODEALIAS'])

for ip_address in ip_list:
  if ip_address in result:
     result[ip_address] += 1
  else:
     result[ip_address] = 1

with open('result.csv', 'w', newline='') as csv_file:
   writer = csv.writer(csv_file)
   for key, value in result.items():
    writer.writerow([key, value])