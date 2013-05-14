# !/usr/bin/python
# -*- coding=UTF-8 -*-

from __future__ import with_statement
import cPickle as pickle

import matplotlib.pyplot as plt


with open("cluster.pkl") as inf:
    samples = pickle.load(inf)     # samples is a list with shape of 3 * 2 * 500

if __name__=="__main__":

    print len(samples)
    for i in range(len(samples)):
        print  ' ', len(samples[i])
        for j in range(len(samples[i])):
            print '  ', len(samples[i][j])

    # plot
    plt.axis([-25, 15, -25, 10])
    plt.scatter(samples[0][0], samples[0][1])
    plt.scatter(samples[1][0], samples[1][1])
    plt.scatter(samples[2][0], samples[2][1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
