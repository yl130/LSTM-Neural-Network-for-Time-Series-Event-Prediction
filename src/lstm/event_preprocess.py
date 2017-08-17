"""
Developed by Pengfei Chen, June 12, 2017.
This class is used to preprocess the event data including vocabulary construction.

"""

import sys
from os.path import dirname, abspath

sys.path.insert(1, dirname(dirname(abspath(__file__))))

class Event_preprocess(object):

     def __init__(self, event_data, separator):
         self.event_data = event_data
         self.separator = separator
         pass

     def construct_vocab(self):
             event_vocab = set(self.event_data)
             event_vocab = sorted(event_vocab)
             return event_vocab

     def vocab_mapping(self):
         event_vocab = self.construct_vocab()
         index_to_vocab = {}
         vocab_to_index = {}
         for i, vocab  in enumerate(event_vocab):
             index_to_vocab[i] = vocab
             vocab_to_index[vocab] = i
         return (index_to_vocab, vocab_to_index)






