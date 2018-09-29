# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the data
dataset = pd.read_csv('Salary_Data.csv')
#index location = iloc
#dataset is a 2d matrix
#select all row in first column
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,1:].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('salary vs Eperience (Training set)')
plt.ylabel('salary')
plt.show()















