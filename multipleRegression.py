
"""importing lib
"""
import pandas as ps
import numpy as np

"""adding data set"""

dataset=ps.read_csv("50_Startups.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values




"""changing column  in city column into binary digit 
 with the help of sklearn.compose import columnTransfer 
 sklearn.preprocessing import onehotencoder
 """
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[3])],remainder="passthrough")
X=np.array(ct.fit_transform(X))


"""Splitting dara set into training set and test test"""
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,Y,train_size=0.2,random_state=0)


print(xtrain)
#print("*******")
#print(help(OneHotEncoder))#
#print(help(ColumnTransformer))