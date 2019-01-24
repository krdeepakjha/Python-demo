# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:59:36 2019

@author: deepajha
"""

# Historams for the iris data and plotting it for the diffeent flowers 
# Using the package seaborn for the visualization 

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

iris_visualization = iris

iris_visualization.columns = ['Sepal_Length', 'Sepal_Width','Petal_Length','Petal_Width','Species']

_ = plt.hist(iris_visualization['Sepal.Length'])  
""" this can be used a dummy variables just to run a while and get to see the plots for a short span of time
"""

_ = plt.xlabel('flowers')
_ = plt.ylabel('Numbers of the flowers')
_ = plt.show()

# Support Vector Machines for classifications

from sklearn import svm
from sklearn.model_selection import train_test_split as split
from sklearn.model_selection import cross_val_score
# Subsetting the data for the training and the testing purpose 

#y = iris_visualization.Species # Dependent variable 
#x = iris_visualization.drop('Sepal_Length', axis = 1) # independent variable.  
x = iris_visualization.drop('Species', axis=1) # Dropping the value to prepare for the training set and testing set. 

#from sklearn.model_selection import train_test_split

iris.target = iris_visualization.Species

train_x, test_x, train_y, test_y = split(x,  iris.target, test_size=0.25, random_state = 0)


iris.clf = svm.SVC(C=1,kernel='linear').fit(train_x,train_y)




#iris_visualization_train = iris_visualization.sample(frac= 0.25)


# Renaming the columns for the analysis 

# 
iris.cross_validation = cross_val_score(iris.clf, x, iris.target, cv= 5)





