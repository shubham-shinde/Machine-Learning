#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:49:40 2018

@author: shubham
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the data
dataset = pd.read_csv('data.csv')

X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 1/4, random_state=0)

#press control+i by selecting variable to see its documentation
#import logistic regression
from sklearn.cluster import KMeans
#assign the number of clusters
k=4

kmeans = KMeans(n_clusters=k)

kmeans = kmeans.fit(dataset)

#prepare test data
X_test = [[4.671, 67], [2.885, 61], [1.666, 90], [5.623, 54], [2.683, 80], [1.875, 60]]

#test the model (returns the cluster number)
y_pred = kmeans.predict(X_test)

#array that contains the cluster number
labels =  kmeans.labels_

#array of size k with co-ordinates of center
centroids = kmeans.cluster_centers_

colors = ['blue', 'red' , 'yellow' , 'green']

# for every elements in the label
y=0
for x in labels:
    #plot the points according the their clusters
    #assign different colors
    plt.scatter(dataset.iloc[y,0], dataset.iloc[y,1], color = colors[x])
    y+=1

for x in range(k):
    #plot the centriods
    lines = plt.plot(centroids[x, 0], centroids[x, 1], 'kx')
    #make the centriods larger
    plt.setp(lines, ms=10.0) #length of line
    plt.setp(lines, mew=1.5) #width of line

title = ('No of clusters (k) = {}' , format(k))
plt.title(title)
plt.xlabel('eruption (mins)')
plt.ylable('waiting (mins)')    
plt.show()