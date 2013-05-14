#!/usr/bin/python
# -*-coding=UTF-8 -*-
 
from PIL import Image
from urllib import urlretrieve
from scipy.cluster.vq import kmeans, vq
from numpy import array, reshape, zeros

def cbk(a, b, c):  
    '''callback function to show the percentage of data loaded.
    a: datablock nums loaded
    b: size of datablock
    c: size of the remote data
    '''  
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print '%.2f%%' % per 
 
print "loading picture..."
urlretrieve('http://www.techcn.com.cn/uploads/200905/s_1242717674yrT9jhc8.jpg', 'exmaple.jpg', cbk)
data = array(Image.open('exmaple.jpg'))
(height, width, channel) = data.shape
data = reshape(data, (height*width, channel))

vqclst = [2, 10, 100, 256]
for k in vqclst:
    print 'Generating vq-%d...' % k
    (centroids, distor) = kmeans(data, k)
    (code, distor) = vq(data, centroids)
    print 'distortion: %.6f' % distor.sum()
    im_vq = centroids[code, :]
    im = Image.fromarray(reshape(im_vq, (height, width, channel)))
    im.show()

