
"""
This class is used to conduct some basic statistics on the event data such as the  distribution of event occurrence,
the number of event.
"""
import csv
import matplotlib.pyplot as plt
class EventStatistics(object):
    def __init__(self, event_file_path):
        self.event_file_path = event_file_path
        pass
    def event_interval_dist(self):
        with open(self.event_file_path) as event_file_handle:
            event_data = csv.DictReader(event_file_handle, delimiter=',')
            time_stamps = []
            for row in event_data:
              time_stamps.append(int(row['FIRSTOCCURRENCE_UTC']))
            event_interval_list = []
            no_of_events = len(time_stamps)
            for index in range(no_of_events-1):
                interval = time_stamps[index+1] - time_stamps[index]
                if interval <= 1440:
                  event_interval_list.append(time_stamps[index+1] - time_stamps[index])
            return  event_interval_list

    def event_interval_plot(self, num_bins):
        event_interval_list = self.event_interval_dist()
        num_bins = num_bins
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(event_interval_list, num_bins, normed=1)
        ax.set_xlabel('event interval   (s)')
        ax.set_ylabel('Probability density')
        ax.set_title(r'event distribution')
        fig.tight_layout()
        plt.show()


    def event_frequency_dist(self):
        with open(self.event_file_path,'r') as event_file_handle:
            event_data = csv.DictReader(event_file_handle, delimiter=',')
            event_list = []
            event_count_list = []
            for row in event_data:
                event_list.append(row['IDENTIFIER'])
            event_set = set(event_list)
            for event in event_set:
                event_count_list.append(event_list.count(event))
            return event_count_list
        pass



    def event_frequency_plot(self, num_bins):
        event_frequency_list = self.event_frequency_dist()
        num_bins = num_bins
        plt.plot(event_frequency_list)
        #fig, ax = plt.subplots()
        #n, bins, patches = ax.hist(event_frequency_list, num_bins, normed=1)
        #ax.set_xlabel('event frequency')
        #ax.set_ylabel('Probability density')
        #ax.set_title(r'event frequency distribution')
        #fig.tight_layout()
        plt.show()

if __name__ == "__main__":
    event_path = "../data/new_event.csv"
    event_statistics = EventStatistics(event_path)
    event_intervals = event_statistics.event_interval_dist()
    for event_interval in event_intervals:
         print (event_interval)
    #event_statistics.event_interval_plot(60)
    event_statistics.event_frequency_plot(100)
    pass
