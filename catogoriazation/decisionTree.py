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
dataset = pd.read_csv('Position_Salaries.csv')
#index location = iloc
#dataset is a 2d matrix
#select all row in first column
#iloc=index location
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:,-1].values

#sklearn is a scikit learn library of py

#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

y_pred = regressor.predict(6.5)

#X_t = np.linspace(0,10,100)
#Y_t = []
#for i in X_t:
#    Y_t.append([i])
#X_t = np.array(Y_t)
#plt.scatter(X, y, color="red")
#plt.plot(X_t, regressor.predict(X_t), color='blue')
#plt.title('salary vs Eperience (Training set)')
#plt.ylabel('salary')
#plt.show()

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.show()














