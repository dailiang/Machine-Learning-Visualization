# !/usr/bin/python
# -*- coding=UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# From 2-D normal distribution, we will get two groups data (x1,y1) 
# and (x2,y2), each with 200 datapoints.

# define covariance matrix and mean values.
m1 = [-5, 0]
m2 = [5, 0]
cov1 = [[1, 0.5], [0.5, 1]]
cov2 = cov1

# Generator random data
np.random.seed(0)
x1,y1 = np.random.multivariate_normal(m1, cov1, 200).T
np.random.seed(1)
x2,y2 = np.random.multivariate_normal(m2, cov2, 200).T

# range the data
nData1 = np.shape(x1)[0]
nData2 = np.shape(x2)[0]
X1 = np.concatenate(([x1], [y1], -np.ones((1,nData1))), axis=0).T
X2 = np.concatenate(([x2], [y2], -np.ones((1,nData2))), axis=0).T
inputs = np.concatenate((X1, X2), axis=0)
# Targets
t1 = np.ones((1, nData1)) 
t2 = -np.ones((1, nData2))
targets = np.concatenate((t1, t2), axis=1).T


if __name__=="__main__":
    # what is the relationship between covariance matrix and shape of distribution?
    eigenval, eigenvec = np.linalg.eig(cov1)
    print "The eigen value of cov matrix is:\n", eigenval
    print "The eigen vector of cov matrix is:\n", eigenvec

    # plot
    plt.axis([-8,8,-6,6])
    plt.plot(x1, y1, 'ro', x2, y2, 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
