#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:42:39 2018

@author: shubham
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the data
dataset = pd.read_csv('KNN.csv')
#index location = iloc
#dataset is a 2d matrix
#select all row in first column
print(dataset.head())
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values
#data preprocessing

#import knn function form sklearn
from sklearn.neighbors import KNeighborsClassifier

#create object
knn = KNeighborsClassifier()

#train the model
knn.fit(X,y)

#prepare the test data
X_test = [[4.9, 7.0, 1.2 , 0.2], [6.0, 2.0, 4.5, 1.5], [6.1, 2.6, 5.6, 1.2]]

#test the model (returns the class)
prediction = knn.predict(X_test)

print(prediction)