

import sys
import os
import csv
import time

from os.path import dirname, abspath
sys.path.insert(1, dirname(dirname(abspath(__file__))))
class add_utc_time():
    def __init__(self):
         pass
    def add_utc_time(self, data_file_path, data_file_path_with_utc):

        data_file_path_handle = open(data_file_path_with_utc, 'w')

        with open(data_file_path,'r') as data_file_handle:
           event_data = csv.DictReader(data_file_handle, delimiter=',')
           header = ','.join(event_data.fieldnames)+',FIRSTOCCURRENCE_UTC'+',LASTOCCURRENCE_UTC' + ',DURATION'
           data_file_path_handle.write(header+"\n")
           for row in event_data:
               temp_str = []
               #print (row['FIRSTOCCURRENCE'][0:-7])
               FIRSTOCCURRENCE_UTC =  time.mktime(time.strptime(row['FIRSTOCCURRENCE'][0:-7],"%Y-%m-%d-%H.%M.%S"))
               LASTOCCURRENCE_UTC =  time.mktime(time.strptime(row['LASTOCCURRENCE'][0:-7],"%Y-%m-%d-%H.%M.%S"))
               DURATION = LASTOCCURRENCE_UTC - FIRSTOCCURRENCE_UTC
               for item in row:
                   temp_str.append(row[item].replace(',','-'))
               data_file_path_handle.write(','.join(temp_str)+','+str(FIRSTOCCURRENCE_UTC)+ ','+ str(LASTOCCURRENCE_UTC)+ ',' + str(DURATION) + '\n')
        data_file_path_handle.close()
        pass

 ### For test
if __name__=="__main__":
    event_data = "..data/event_d_client_id_299.csv"
    new_event_data = "..data/new_event.csv"
    add_utc_time_inst = add_utc_time()
    add_utc_time_inst.add_utc_time(event_data,new_event_data)


