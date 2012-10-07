#!/usr/bin/env python

import csv
import data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.hmm import GaussianHMM

if __name__ == "__main__":

    data_dir = './data/'
    train_data = 'train.csv'
    train = open(data_dir + train_data, 'rb')
    t = list(csv.reader(train))
    entries = len(t) - 1
    
    farm1 = data.farm('wp1', entries)
    farm2 = data.farm('wp2', entries)
    farm3 = data.farm('wp3', entries)
    farm4 = data.farm('wp4', entries)
    farm5 = data.farm('wp5', entries)
    farm6 = data.farm('wp6', entries)
    farm7 = data.farm('wp7', entries)

    
    for i, row in enumerate(t[1:]):
        farm1.fill(i, row[0], row[1])
        farm2.fill(i, row[0], row[2])
        farm3.fill(i, row[0], row[3])
        farm4.fill(i, row[0], row[4])
        farm5.fill(i, row[0], row[5])
        farm6.fill(i, row[0], row[6])
        farm7.fill(i, row[0], row[7])    

    model = GaussianHMM(algorithm='viterbi', covariance_type='full', covars_prior=0.01,
      covars_weight=1, means_prior=None, means_weight=0, n_components=5,
      random_state=None, startprob=None, startprob_prior=1.0,
      transmat=None, transmat_prior=1.0)

    print "Fitting model..."
    
    model.fit([farm1.get_output()], n_iter = 1000)

    print "Predicting hidden states..."
    hidden_states = model.predict(farm1.get_output())

    print "Transition matrix"
    print model.transmat_
    print ""
    print "mean and vars of the hidden states"
    for i in range(5):
        print "%dth hidden state" % i
        print "mean = ", model.means_[i]
        print "var = ", np.diag(model.covars_[i])
        print ""
