# !/usr/bin/python
# -*- coding=UTF-8 -*-

import copy as cp
import matplotlib.pyplot as plt
import numpy as np

from data import *

def lms_alg(inputs, targets, eta=0.05, weights=np.random.rand(3,1)*0.1 - 0.05, nIteration=1):
    ''' eta is learning rate '''
    weights_start = cp.deepcopy(weights)
    # n iteration
    for n in range(nIteration):
        outputs = np.dot(inputs, weights)
        # Threshold the outputs
        weights += eta/(nData1+nData2)*np.dot(inputs.T, targets-outputs)
    outputs = np.dot(inputs, weights)
    # Threshold the outputs
    outputs = np.where(outputs>0,1,-1) 
    return (outputs,weights_start, weights)

if __name__=="__main__":
    final = lms_alg(inputs, targets, nIteration=8)
    
    outputs_final = final[0] - targets
    outputs_final = np.where(outputs_final==0, 0, 1)
    nMis = sum(outputs_final)
    print 'Num of misclassified:'
    print nMis
    weights_start = final[1]
    weights = final[2]
    outputs = np.dot(inputs, weights)
    # 统计误分点的个数 
    outputs = np.dot(inputs, weights)
    # 求Loss
    Loss = sum((targets-outputs)**2)
    print 'Init Weight:'
    print weights_start
    print 'Final Weight:'
    print weights
    print 'Loss:'
    print Loss
    
    # plot
    classfier_x = np.linspace(-8, 8, 100)
    classfier_y = (weights[2] - weights[0]*classfier_x)/weights[1]
    classfier_y_start = (weights_start[2] - weights_start[0]*classfier_x)/weights_start[1]
    plt.axis([-8,8,-6,6])
    plt.plot(x1, y1, 'ro', x2, y2, 'bo')
    plt.plot(classfier_x, classfier_y_start, 'm--', classfier_x, classfier_y, 'g-')
    plt.legend(["+1", "-1", "Init", "Final"])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
