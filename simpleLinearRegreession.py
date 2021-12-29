"""
importing libraries
"""

import pandas as ps
import matplotlib.pyplot as pt


dataset=ps.read_csv("Salary_Data.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

"""
splitting dataset into test set and training set"""

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,Y, train_size=1/3,random_state=0)

""" model regressiion"""
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(xtrain,ytrain)


""" drawing predicted value used by regressor"""

pt.scatter(xtrain,ytrain,color="red")
pt.plot(xtrain,regressor.predict(xtrain),color="blue")
pt.title("Vishnu 2nd ML/AI")
pt.xlabel("Emp ages")
pt.ylabel("Emp's salaries")
pt.show()


""" drawing test reslult prediction , above is trainig set"""
pt.scatter(xtest,ytest,color="green")
pt.plot(xtrain,regressor.predict(xtrain),color="purple")
pt.title("vishnu 3rd image ML")
pt.xlabel("Emo;s ages")
pt.ylabel("Emps Salary")
pt.show()





"""find salary for 12 years means"""
print("12 yrs salary :",regressor.predict([[12]]))

"""find coefficient & interception"""
print("Cooeff :",regressor.coef_)
print("Intercept :",regressor.intercept_)


