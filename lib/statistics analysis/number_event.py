import csv
import sys
from imp import reload
reload(sys)
import importlib
importlib.reload(sys)


event_list = []
result = {}

with open('../data/test2.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
   event_list.append(row['INSTANCESITUATION'])
   #print (row['INSTANCESITUATION'])

for event in event_list:
  if event in result:
      result[event] += 1
  else:
      result[event] = 1

with open('result.csv', 'w', newline='') as csv_file:
  writer = csv.writer(csv_file)
  for key, value in result.items():
      writer.writerow([key,value])
