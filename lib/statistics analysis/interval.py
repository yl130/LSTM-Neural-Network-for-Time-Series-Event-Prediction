#the interval of event occurrence

import csv
import sys
from imp import reload
reload(sys)
import importlib
importlib.reload(sys)


event_interval = []
time_stamps = []
output={}
index_count = 0

with open('../data/event.csv') as csvfile:
  reader = csv.DictReader(csvfile,delimiter=',')
  for row in reader:
      time_stamps.append(int(row['FIRSTOCCURRENCE_UTC']))
      no_of_events = len(time_stamps)
  for index in range(no_of_events - 1):
      #interval = time_stamps[index + 1] - time_stamps[index]
      event_interval.append(time_stamps[index + 1] - time_stamps[index])
  print (event_interval)

with open('../data/event.csv') as csvfile:
   with open('Output.csv', 'w', newline='') as csv_file:
         reader = csv.DictReader(csvfile,delimiter=',')
         writer = csv.writer(csv_file)
         header = reader.fieldnames
         print(header.append('Interval'))
         writer.writerow(header)
         for row in reader:
               row_values = []
               row['Interval'] = event_interval[index_count]
               if index_count + 1 < len(event_interval):
                    index_count = index_count + 1
                    #print(row.keys())
                    #print(row.values())
                    row_values.append(row['INSTANCESITUATION'])
                    row_values.append(row['FIRSTOCCURRENCE_UTC'])
                    #row_values.append(event_interval[index_count])
                    row_values.append(row['Interval'])
                    writer.writerow(row_values)
                    #writer.writerow(row.values())



