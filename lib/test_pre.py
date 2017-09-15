
Naive LSTM to learn one time step to one mapping
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils
# fix random seed for reproducibility
#numpy.random.seed(7)
# define the raw dataset
with open('/home/yl130/EventAnalysis/EventAnalysis/data/training.txt', 'r') as event_data_handle:
  event_sequence = event_data_handle.read()
# create mapping of characters to integers (0-25) and the reverse
char_to_int = dict((c, i) for i, c in enumerate(event_sequence))
int_to_char = dict((i, c) for i, c in enumerate(event_sequence))
print(char_to_int)
