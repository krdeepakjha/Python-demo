# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:24:52 2019

@author: deepajha
"""

# Decision Tree with the 
import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree


from rpy2.robjects import r, pandas2ri
def data(iris): 
    return pandas2ri.ri2py(r[iris])
iris = data('iris')




#iris = load_iris()

iris.data = iris.drop(['Species'],axis =1)

iris_decision_target = iris['Species']
# Calculating the decision tree for the available iris data 

decision = tree.DecisionTreeClassifier()

decision.iris = decision.fit(iris.data, iris_decision_target)

############

"""
Visualizing the decision tree for the iris data. 
"""

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydo


dot_data = StringIO()

export_graphviz(decision, out_file=dot_data, filled=True, rounded=True, special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())






