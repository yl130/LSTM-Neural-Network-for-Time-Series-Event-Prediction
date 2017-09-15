
### This file aims to analyze the event correlation with harwke point process ####
from  pyhawkes import models
import numpy as np
import csv
import time

event_file_path = "../data/new_event_composed_alert_name_data.csv"

### Load data from csv file. ###

with open(event_file_path,'r') as event_file_handle:
    event_data = csv.reader(event_file_handle, delimiter = ',')
    next(event_data)
    event_data_array = np.array([[int(col) for col in row] for row in event_data])
    print (event_data_array.shape)
    event_data_array = event_data_array[0:40000,0:10]

no_of_events = event_data_array.shape[1]
no_of_points = event_data_array.shape[0]
print ((no_of_events, no_of_points))


#### Setting parameters. ####

p = 0.05
dt_max = 2
network_hypers = {"p": p, "allow_self_connections": True}
train_model = models.DiscreteTimeNetworkHawkesModelSpikeAndSlab(K=no_of_events, dt_max=7, network_hypers=network_hypers)
train_model.add_data(event_data_array)
fig, test_handles = train_model.plot(color="#e41a1c")
train_model.plot(handles=test_handles)
time.sleep(10)

#####  Run a Gibbs sampler.  #####
N_samples = 150
lps = []
for itr in range(N_samples):
    train_model.resample_model()
    lps.append(train_model.log_probability())
    train_model.plot(handles=test_handles)
time.sleep(100)




"""
true_model = models.DiscreteTimeNetworkHawkesModelSpikeAndSlab(
    K=K, dt_max=dt_max, network_hypers=network_hypers)

# Generate T time bins of events from the the model
# S is the TxK esvent count matrix, R is the TxK rate matrix
S,R = true_model.generate(T=300)
true_model.plot()

# Create the test model, add the event count data, and plot
test_model = models.DiscreteTimeNetworkHawkesModelSpikeAndSlab(
    K=K, dt_max=dt_max, network_hypers=network_hypers)
test_model.add_data(S)
fig, test_handles = test_model.plot(color="#e41a1c")

# Run a Gibbs sampler
N_samples = 100
lps = []
for itr in range(N_samples):
    test_model.resample_model()
    lps.append(test_model.log_probability())

    # Update plots
    #test_model.plot(handles=test_handles)
time.sleep(10)
"""
