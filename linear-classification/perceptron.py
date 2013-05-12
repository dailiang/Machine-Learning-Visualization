# !/usr/bin/python
# -*- coding=UTF-8 -*-

import copy as cp

from data import *

# Since Loss function is:
#     Loss(w) = sum( sign(Xw)*(Xw-target))   X belongs to misclassified datapoint
# using gradient descent algorithm:
#        Gradient of w = sign(Xw) * X

def pcn_train(inputs, targets, eta=0.25, weights=np.random.rand(3,1)*0.1 - 0.05, nIteration=1):
    ''' perceptron training phase, eta is learning rate '''
    weights_start = cp.deepcopy(weights)
    for n in range(nIteration):
        """ Run the network forward """
        outputs = np.dot(inputs, weights)
        # Threshold the outputs
        outputs = np.where(outputs>0,1,-1)
        weights += eta*np.dot(inputs.T,targets-outputs)
    # outputs    
    outputs = np.dot(inputs, weights)
    # Threshold the outputs
    outputs = np.where(outputs>0,1,-1)
    return (outputs,weights_start, weights)

if __name__=="__main__":
    '''train'''
    final = pcn_train(inputs, targets, nIteration=4)
    outputs_final = final[0] - targets
    outputs_final = np.where(outputs_final==0, 0, 1)
    nMis = sum(outputs_final)
    print 'Nums of data that is misclassifed:'
    print nMis
    weights_start = final[1]
    weights = final[2]
    print 'The init weights:'
    print weights_start
    print 'The finally weights:'
    print weights

    # plot
    classfier_x = np.linspace(-8, 8, 100)
    classfier_y = (weights[2] - weights[0]*classfier_x)/weights[1]
    classfier_y_start = (weights_start[2] - weights_start[0]*classfier_x)/weights_start[1]
    plt.axis([-8,8,-6,6])
    plt.plot(x1, y1, 'ro', x2, y2, 'bo')
    plt.plot(classfier_x, classfier_y_start, 'm--', classfier_x, classfier_y, 'g-')
    plt.legend(['+1', '-1', 'init', 'fianl'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
