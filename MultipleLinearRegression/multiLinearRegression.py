
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the data
dataset = pd.read_csv('50_Startups.csv')
#index location = iloc
#dataset is a 2d matrix
#select all row in first column
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,4].values
#data preprocessing

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
#to remove deficulty of graph plotting between string and int we convert string to int
#labelencoder converts cities name to 1,2 & 3
X[:,3] = labelencoder.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()
#hotencoder converted 1, 2 & 3 into binary inputs making 3 new rows and deleting one
X=X[:,1:]

#now splitting data into trainning and testing data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 1/3, random_state=0)

#now import Linear Regression model from scikit learn
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train[:,-1], y_train, color="red")
plt.plot(X_train[:,-1], regressor.predict(X_train), color='blue')
plt.title('salary vs Eperience (Training set)')
plt.ylabel('salary')
plt.show()