

import sys
import os
from keras.models import Sequential, Model
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.recurrent import LSTM, GRU, SimpleRNN
from keras.layers import Input
from keras.utils.data_utils import get_file
from keras.optimizers import rmsprop
from keras.optimizers import Nadam
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.layers.normalization import BatchNormalization
from datetime import datetime
from math import log


class Model_building(object):

    def __init__(self):
        #self.output_unit = output_unit
        #self.input_shape = input_shape
        pass
    def build_model(self, output_unit, input_shape, drop_out):
        model = Sequential()
        model.add(LSTM(output_unit, return_sequences=True, input_shape=(input_shape[0], input_shape[1])))
        model.add(Dropout(drop_out))
        model.add(LSTM(output_unit, return_sequences=False))
        model.add(Dropout(drop_out))
        model.add(Dense(input_shape[1]))
        model.add(Activation('sigmoid'))
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=['accuracy'])

        with open('keras-lstm-event-model.json', 'w') as f:
            f.write(model.to_json())
        return model

if __name__ == "__main__":
    output_unit = 512
    input_shape = (20, 330)
    drop_out=0.2
    #model_building = Model_building(output_unit,input_shape,drop_out)
    model_building = Model_building()
    model_building.build_model(output_unit,input_shape,drop_out)



