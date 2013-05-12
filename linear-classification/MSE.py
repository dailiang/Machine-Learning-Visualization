# !/usr/bin/python
# -*- coding=UTF-8 -*-

from data import *

# W = (XX^T)^{-1}XT

t1 = np.ones((1, nData1)) 
t2 = -np.ones((1, nData2))
targets = np.concatenate((t1, t2), axis=1).T
X = inputs
weights = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, targets))

if __name__=="__main__":
    outputs = np.dot(X, weights)
    # Loss
    Loss = sum((targets - outputs)**2)
    # Threshold the outputs
    outputs = np.where(outputs>0,1,-1)
    outputs -= targets
    outputs = np.where(outputs==0, 0, 1)
    nMis = sum(outputs)
    print 'Num of miclassifed datapoint:'
    print nMis
    print 'Final weights:'
    print weights
    print 'Loss:'
    print Loss
    
    
    # plot
    classfier_x = np.linspace(-8, 8, 100)
    classfier_y = (weights[2] - weights[0]*classfier_x)/weights[1]
    plt.axis([-8,8,-6,6])
    plt.plot(x1, y1, 'ro', x2, y2, 'bo')
    plt.plot(classfier_x, classfier_y, 'g-')
    plt.legend(['+1', '-1'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
