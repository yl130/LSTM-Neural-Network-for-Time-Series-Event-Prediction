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
    #print (seq_in, '->', seq_out)
# reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (len(dataX), seq_length, 1))
# normalize
#X = X / float(len(event_sequence))
# one hot encode the output variable
y= np_utils.to_categorical(dataY)

# create and fit the model
batch_size = 1
model = Sequential()

model.add(LSTM(16, batch_input_shape=(batch_size, X.shape[1], X.shape[2]), stateful=True))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

for i in range(300):
	model.fit(X, y, epochs=10, batch_size=batch_size, verbose=2, shuffle=False)
	model.reset_states()
# summarize performance of the model
scores = model.evaluate(X, y, batch_size=batch_size, verbose=0)
model.reset_states()
print("Model Accuracy: %.2f%%" % (scores[1]*100))
# demonstrate some model predictions
seed = [char_to_int[event_sequence[0]]]
for i in range(0, len(event_sequence)-1):
	x = np.reshape(seed, (1, len(seed), 1))
	x = x / float(len(event_sequence))
	prediction = model.predict(x, verbose=0)
	index = np.argmax(prediction)
	print (int_to_char[seed[0]], "->", int_to_char[index])
	seed = [index]
model.reset_states()
# demonstrate a random starting point
letter = "21"
seed = [char_to_int[letter]]
print("New start: ", letter)
for i in range(0, 5):
	x = np.reshape(seed, (1, len(seed), 1))
	x = x / float(len(event_sequence))
	prediction = model.predict(x, verbose=0)
	index = np.argmax(prediction)
	print (int_to_char[seed[0]], "->", int_to_char[index])
	seed = [index]
model.reset_states()