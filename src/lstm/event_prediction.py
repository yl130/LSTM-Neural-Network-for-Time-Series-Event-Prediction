"""
Developed by Pengfei Chen, June 10, 2017.
In this class, we will leverage mxnet to predict
"""

from __future__ import print_function, unicode_literals, division
import random
import sys
import os
import codecs

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
import numpy as np

event_corpus = "../data/test_data.txt"






