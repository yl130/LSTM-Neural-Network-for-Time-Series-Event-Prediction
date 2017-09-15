
import numpy as np
from keras.models import Model
import random
from src.lstm.event_preprocess import Event_preprocess
from src.lstm.gen_train_data import Gen_train_data
import sys
from os.path import dirname, abspath
sys.path.insert(1, dirname(dirname(abspath(__file__))))

class Model_training(object):
    def __init__(self, model, max_seed_length, sequence_length, event_data, separator):
        self.seed_length = sequence_length
        self.max_seed_length = max_seed_length
        self.no_of_events = len(event_data)
        self.sequence_length = sequence_length
        self.event_data = event_data
        self.separator = separator
        self.model = model
        pass

    def sample(self, a, temperature=1.0):

        a = np.log(a)/temperature
        a = np.exp(a)/np.sum(np.exp(a))
        for i, val  in enumerate(a):
            if val < 1e-5:
                a[i] = 0
        print (a)
        #return np.argmax(a)
        return np.argmax(np.random.multinomial(30,a,1))

    def predict(self, seed=None, predict_length=10, diversity=0.8):
        initial_seed_length = self.seed_length
        max_seed_length = self.max_seed_length

        print("\n")
        if seed:
           seed_sequence  = seed
        else:
           start_index  = random.randint(0, self.no_of_events - self.sequence_length - 1)
           seed_sequence = self.event_data[start_index:(start_index + initial_seed_length)]

        print('Generating with seed: "{}"'.format(seed_sequence))
        print('\n{}'.format(seed_sequence), end=' ')
        prediction = []
        event_preprocess = Event_preprocess(self.event_data, self.separator)
        (index_to_vocab, vocab_to_index) = event_preprocess.vocab_mapping()
        vocabs = event_preprocess.construct_vocab()
        vocabs_size = len(vocabs)

        for i in range(predict_length):
            x = np.zeros((1, len(seed_sequence), vocabs_size))

            ### Set one-hot vectors for seed sequences
            for t, event in enumerate(seed_sequence):
                x[0,t,vocab_to_index[event]] = 1


            preds =  self.model.predict(x, verbose=0)[0]

            next_index = self.sample(preds, diversity)
            next_event = index_to_vocab[next_index]
            prediction.append(next_event)

            seed_sequence = seed_sequence[1:]
            seed_sequence.append(next_event)
            #print ("New sequence")
            #print (seed_sequence)
            #print ("next event is")
            #print (next_event, end=' ')
            sys.stdout.flush()
        prediction = ' '.join(prediction)
        #sys.stdout.flush()
        return prediction

    def train(self, training_data):
         iteration  = 1
         X = training_data[0]
         Y = training_data[1]
         for iteration in range(iteration, 5):
             #print('Iteration {}'.format(iteration))
             self.model.fit(X, Y, batch_size=128, epochs=50)

             # Output an example after 100 epochs of training.
             #self.predict()

             # Save the trained weights.
             # This is done periodically during training in case the computer crashes.
             self.model.save_weights('keras-lstm-event-weights.h5')




