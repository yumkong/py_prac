# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 22:05:24 2016

@author: yumkong
"""
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixles assigned to each cluster
    numlabels = np.arange(0, len(np.unique(clt.labels_))+1)
    (hist, _) = np.histogram(clt.labels_, bins = numlabels)
    #normalize the histgraom, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
    #return the histogram
    return hist

image = cv2.imread("v1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#resize it
h, w, _ = image.shape
w_new = int(100 * w / max(w, h))
h_new = int(100 * h / max(w, h))

image = cv2.resize(image, (w_new, h_new))
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixles
image_array = image.reshape((image.shape[0] * image.shape[1], 3))

#clustering the pixles
clt = KMeans(n_clusters = 3)
clt.fit(image_array)

# finds how many pixels are in each cluster
hist = centroid_histogram(clt)

#sort the clusters according to how many pixel they have
zipped = zip(hist, clt.cluster_centers_)
zipped.sort(reverse=True, key=lambda x:x[0])
hist, clt_cluster_centers_ = zip(*zipped)


    
