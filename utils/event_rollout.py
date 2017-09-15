"""

This class is used to roll out the events along with time.
"""
import os
import csv
import numpy as np

class Event_rollout(object):
    def __init__(self, normalized_event_file):
        self.normalized_event_file = normalized_event_file

    def rollout(self,output_file):
        output_file_handle = open(output_file,'w')
        with open(self.normalized_event_file,'r') as normalized_event_file_handle:
             event_data = csv.reader(normalized_event_file_handle,delimiter = ',')
             next(event_data)
             event_data_array = np.array([[(col) for col in row] for row in event_data])
        no_of_events = event_data_array.shape[1]
        no_of_points = event_data_array.shape[0]
        event_seq = []
        for row in range(no_of_points):
            row_values = [int(x) for x in event_data_array[row]]
            if np.sum(row_values)  == 0:
                event_seq.append("NOP")
            else:
                for col in range(no_of_events):
                   if event_data_array[row][col] == '1':
                       #print (col)
                       event_seq.append(str(col))

        output_file_handle.write(' '.join(event_seq))
        output_file_handle.close()


if __name__ == "__main__":
    normalized_event_file = '/Users/chenpengfei/Documents/ResearchInIBM/SDI/EventCorrelation/rawdata/client_299/ReducedEventSet.csv'
    output_file = '/Users/chenpengfei/Documents/ResearchInIBM/SDI/EventCorrelation/rawdata/client_299/reduced_event_seq.txt'
    event_rollout = Event_rollout(normalized_event_file)
    event_rollout.rollout(output_file)
    pass
