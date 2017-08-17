"""
Developed by Pengfei Chen, June 13, 2017.
This file is used to test the effectiveness of LSTM.
"""

from keras.models import Model
from src.lstm.gen_train_data import Gen_train_data
from src.lstm.model_building import Model_building
from src.lstm.training import Model_training



#### Initialization of traning  event data generization

event_data_file = "/home/yl130/EventAnalysis/EventAnalysis/data/training.txt"
separator = ' '
event_sequence_length = 1
step = 1

### Initialization of model building

output_unit = 512
drop_out = 0.2

### Obtain event data

with open(event_data_file, 'r') as event_data_file_handle:
    event_data = event_data_file_handle.read()
    event_data_list = event_data.split(' ')
g_train_data = Gen_train_data(event_data_list, separator)

vocabs = g_train_data.get_vocab()


vocabs_size = len(vocabs)

training_data = g_train_data.gen_train_data(event_sequence_length, step)

input_shape = (event_sequence_length, vocabs_size)

### Building model
m_building = Model_building()
model = m_building.build_model(output_unit,input_shape,drop_out)

### Event model training and prediction

max_seed_length = 1
m_training = Model_training(model, max_seed_length, event_sequence_length, event_data_list, separator)
m_training.train(training_data)

weights_file = "keras-lstm-event-weights.h5"

model.load_weights(weights_file)

predict_result = m_training.predict(seed=['21'])
print(predict_result)














