
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
xtrain,xtest,ytrain,ytest=train_test_split(X,Y,train_size=0.1,random_state=1)

"""Regression prediction started"""
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(xtrain,ytrain)

print("xtrain :",xtrain)
print("**** X trin Over ****")

#print("Ytrain : ",ytrain)


np.set_printoptions(precision=2)# precise 2 digit in decimal
ypred=regressor.predict(xtest )




print("Prediction xtrain :",ypred)

print("*******")

print("Actual result :",ytest)

""" comparing both output , y pred is predicted and ytest is given dependebt variable"""


#print(np.concatenate(ypred+ytest))






#print(help(OneHotEncoder))#
#print(help(ColumnTransformer))