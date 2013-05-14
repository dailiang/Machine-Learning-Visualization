# !/usr/bin/python
# -*- coding=UTF-8 -*-


from numpy import zeros, array, tile
from scipy.linalg import norm
import numpy.matlib as ml
import random

from data import *

def kmeans(X, k, observer=None, threshold=1e-15, maxiter=300):
    '''
    Cluster and show data X
    X: N * 2 array, data to be clustered
    k: k means
    observer: the plot function
    '''
    N = len(X)
    labels = zeros(N, dtype=int)
    centers = array(random.sample(X, k))   # Choose k unique elements from X
    iter = 0
 
    def calc_J():
        sum = 0
        for i in xrange(N):
            sum += norm(X[i]-centers[labels[i]])
        return sum
 
    def distmat(X, Y):
        n = len(X)
        m = len(Y)
        xx = ml.sum(X*X, axis=1)
        yy = ml.sum(Y*Y, axis=1)
        xy = ml.dot(X, Y.T)
 
        return tile(xx, (m, 1)).T+tile(yy, (n, 1)) - 2*xy
 
    Jprev = calc_J()
    while True:
        # notify the observer
        if observer is not None:
            observer(iter, labels, centers)
 
        # calculate distance from x to each center
        # distance_matrix is only available in scipy newer than 0.7
        # dist = distance_matrix(X, centers)
        dist = distmat(X, centers)
        # assign x to nearst center
        labels = dist.argmin(axis=1)
        # re-calculate each center
        for j in range(k):
            idx_j = (labels == j).nonzero()
            centers[j] = X[idx_j].mean(axis=0)
 
        J = calc_J()
        iter += 1
 
        if Jprev-J < threshold:
            break
        Jprev = J
        if iter >= maxiter:
            break
 
    # final notification
    if observer is not None:
        observer(iter, labels, centers)
 
if __name__ == '__main__':
    N = 0
    for smp in samples:
        N += len(smp[0])
    X = zeros((N, 2))
    # put all data into X
    idxfrom = 0
    for i in range(len(samples)):
        idxto = idxfrom + len(samples[i][0])
        X[idxfrom:idxto, 0] = samples[i][0]
        X[idxfrom:idxto, 1] = samples[i][1]
        idxfrom = idxto
 
    def observer(iter, labels, centers):
        print "iter %d." % iter
        colors = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        plt.plot(hold=False)  # clear previous plot
        plt.hold(True)
 
        # draw points
        data_colors=[colors[lbl] for lbl in labels]
        plt.scatter(X[:, 0], X[:, 1], c=data_colors, alpha=0.5)
        # draw centers
        plt.scatter(centers[:, 0], centers[:, 1], s=200, c=colors)
        plt.show()
 
        # plt.savefig('iter_%02d.png' % iter, format='png')
 
    kmeans(X, 3, observer=observer)

