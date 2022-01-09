#"""polynomial Regression as example as salary of emps"""

"""importing libraries"""

import pandas as ps
import matplotlib.pyplot as pt
import numpy as np

dataset=ps.read_csv("Position_Salaries.csv")
X=dataset.iloc[:,1:-1].values
Y=dataset.iloc[:,-1].values


"""Trainng Linear regression set"""
from sklearn.linear_model import LinearRegression

linear=LinearRegression()
#linear.fit(X,Y)

"""Polynomial start from here"""
# from sklearn.preprocessing import PolynomialFeatures
# polynomial = PolynomialFeatures(degree=7) #"""We need to convert single matrix to multi Dinmension matrix Due to polynomial Powers"""
# X_Poly = polynomial.fit_transform(X)
# linear2=LinearRegression()
# linear2.fit(X_Poly,Y)

"""Visulaising each regression """

# pt.scatter(X,Y,color="red")
# pt.plot(X,linear.predict(X),color="blue")
# pt.title("Salary in Linear")
# pt.xlabel("Exp")
# pt.ylabel("Salary")
# pt.show()


"""Visulaising polyimage in plyplot"""

# pt.scatter(X,Y,color="red")
# pt.plot(X,linear2.predict(X_Poly ),color="green")
# pt.title("Polynomial regressoin")
# pt.xlabel("years in experience")
# pt.ylabel("Salary")
# pt.show()

"""Visualizing smoother curve"""

# np_grid=np.arange(min(X),max(X),0.1)
# np_grid=np_grid.reshape(len(np_grid),1)
# pt.scatter(X,Y,color="blue")
# pt.plot(np_grid,linear2.predict(polynomial.fit_transform( np_grid)),color="red")
# pt.title("for smoother curve")
# pt.xlabel("exp")
# pt.ylabel("salary")
# pt.show()


print(dataset.shape)
print(dataset.head())
print(dataset.info())
print("*******")
print(dataset.isnull())
print("$$$$$$$")
print(dataset.Salary.value_counts())







