import csv
import sys
from imp import reload
reload(sys)

import importlib
import np_utils

importlib.reload(sys)

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils

event_t = np.loadtxt('../data/training_data.txt', delimiter=',', usecols=(0,), dtype=str)
#event_t = list(map(int,event_t))
print(event_t)
#thefile = open('../data/training.txt', 'w')
#for item in event_t:
    #thefile.write("%s " % item)


#with open('/home/yl130/EventAnalysis/EventAnalysis/data/training.txt', 'r') as event_data_handle:
  #event_sequence = event_data_handle.read()
  #print(event_sequence)
event_sequence = event_t
# create mapping of characters to integers (0-25) and the reverse
char_to_int = dict((c, i) for i, c in enumerate(event_sequence))
int_to_char = dict((i, c) for i, c in enumerate(event_sequence))
print(char_to_int)
print(int_to_char)

seq_length = 1
dataX = []
dataY = []
for i in range(0, len(event_sequence) - seq_length, 1):
    seq_in = event_sequence[i:i + seq_length]
    seq_out = event_sequence[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
    print (seq_in, '->', seq_out)
# reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (len(dataX), seq_length, 1))
# normalize
#X = X / float(len(event_sequence))
# one hot encode the output variable
y= np_utils.to_categorical(dataY)

# create and fit the model
model = Sequential()

model.add(LSTM(32, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=50, batch_size=128, verbose=2)

# summarize performance of the model
scores = model.evaluate(X, y, verbose=0)
print("Model Accuracy: %.2f%%" % (scores[1] * 100))

# demonstrate some model predictions
for pattern in dataX:
  x = np.reshape(pattern, (1, len(pattern), 1))
  x = x / float(len(event_sequence))
  prediction = model.predict(x, verbose=0)
  index = np.argmax(prediction)
  result = int_to_char[index]
  seq_in = [int_to_char[value] for value in pattern]
  print(seq_in, "->", result)