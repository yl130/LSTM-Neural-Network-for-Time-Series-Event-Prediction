import csv
import sys
from imp import reload

reload(sys)
import numpy as np
import importlib

importlib.reload(sys)


event_t = np.loadtxt('../data/training_data.txt', delimiter=' ', usecols=(0,), dtype=str)
event_t = list(map(int,event_t))
print(event_t)
thefile = open('../data/training.txt', 'w')
for item in event_t:
    thefile.write("%s " % item)


event_test = np.loadtxt('../data/test_data.txt', delimiter=' ', usecols=(0,), dtype=str)
event_test = list(map(int,event_test))
print(event_test)

thefile = open('../data/test.txt', 'w')
for item in event_test:
    thefile.write("%s " % item)