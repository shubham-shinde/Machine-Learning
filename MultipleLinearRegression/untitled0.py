
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the data
dataset = pd.read_csv('50_Startups.csv')
#index location = iloc
#dataset is a 2d matrix
#select all row in first column
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:,1:].values