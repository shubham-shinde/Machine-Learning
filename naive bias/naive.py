#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:50:52 2018

@author: shubham
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the data
dataset = pd.read_csv('cancer.csv')
#index location = iloc
#dataset is a 2d matrix
#select all row in first column
print(dataset.head())
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,-1].values
#data preprocessing

#import knn function form sklearn
from sklearn.naive_bayes import GaussianNB

#create object
naive = GaussianNB()

#train the model
naive.fit(X,y)

#prepare the test data
X_test = [[12, 70, 12], [13, 20, 13]]

#test the model (returns the class)
prediction = naive.predict(X_test)

print(prediction)