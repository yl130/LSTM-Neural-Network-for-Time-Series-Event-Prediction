"""
Developed by Pengfei Chen, June 12, 2017
"""

import sys
import numpy as np
from os.path import dirname, abspath

from src.lstm.event_preprocess import Event_preprocess

sys.path.insert(1, dirname(dirname(abspath(__file__))))

class Gen_train_data(object):
    def __init__(self, event_data, separator):
        self.event_data = event_data
        self.separator = separator
        self.e_preprocess = Event_preprocess(self.event_data, separator)

    def get_vocab(self):
        return self.e_preprocess.construct_vocab()


    def gen_train_data(self, event_sequence_length, step):
        event_sequences = []
        next_event = []
        no_of_event = len(self.event_data)
        vocabs = self.get_vocab()
        vocab_size = len(vocabs)
        (index_to_vocab, vocab_to_index) = self.e_preprocess.vocab_mapping()
        for i  in range(0, no_of_event - event_sequence_length, step):
            event_sequences.append(self.event_data[i:i + event_sequence_length])
            next_event.append(self.event_data[i+event_sequence_length])
        no_of_sequences = len(event_sequences)
        X = np.zeros((no_of_sequences, event_sequence_length, vocab_size), dtype = np.bool)
        Y = np.zeros((no_of_sequences,vocab_size), dtype=np.bool)

        for i, sequence in enumerate(event_sequences):
            for j, event in enumerate(sequence):
                X[i,j,vocab_to_index[event]] = 1
            Y[i,vocab_to_index[next_event[i]]] = 1
        return (X, Y)


if __name__ == "__main__":
    event_data_file = "/home/yl130/EventAnalysis/EventAnalysis/data/event.txt"
    separator = ' '
    event_sequence_length = 10
    step = 3
    with open(event_data_file, 'r') as event_data_file_handle:
        event_data = event_data_file_handle.read()
        event_data_list = event_data.split(' ')
    gen_train_data = Gen_train_data(event_data_list, separator)
    (X,Y) = gen_train_data.gen_train_data(event_sequence_length, step)
    pass