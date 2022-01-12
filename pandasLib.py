"""Pandas Lib  for data preprocessing and analysis & main tool in ML .
    Pandas tool frame were 2d frame with rows and columns"""
import random

import pandas as ps
import numpy as np

"""Creating pandas data frame"""
from sklearn.datasets import load_diabetes

boston_dataset=load_diabetes()
#boston_dataset.to_csv("diabetic.csv")

#print(boston_dataset) # if you see output its not structured , so y pandas came into play


b_dt=ps.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)

print(b_dt.head())
print(b_dt.info)


"""Creating from reading CSV file"""
dt=ps.read_csv("Data.csv")

"""Reading from excel"""
#a=ps.read_excel("")
"""Convert file to Csv file """

a=b_dt.head()
#a.to_csv("vichu.csv")

"""Same as for excel , json """

"""We can create a random data frame variable"""
b=ps.DataFrame(np.random.randint(10,20,(19,10)))
print(b.shape) #row * col
print(b.tail()) #last 5 rows
print(b.info()) # info , info() is different


"""Finding missing value in data frame"""
print(b_dt.isnull().sum()) #0 represents all values filled (NA , _  not there)

"""if we need to count value based on output For ex : 0 ,1 if its in OP then,"""
"""Group value based in labeled column"""
print(b_dt.value_counts("age"))

"""Group value based on mean"""
print(b_dt.groupby("age").mean())

"""Group value based on median value"""
print(b_dt.groupby("age").median())


"""We can see statistical value in pandas"""
print(b_dt.count( ))

"""We can see mean value by  each column wise"""

print(b_dt.mean())


"""checking std deviation """
print(b_dt.std())

"""printing min and max value"""

print(b_dt.min())
print(b_dt.max())


"""describing all statistical value"""

print(b_dt.describe())


"""adding a column in data set"""
#b_dt["newColumn"]=boston_dataset.target new column and target shld have same length

"""removing a row"""
print(b_dt.head())
b_dt.drop(index=0,axis=1,inplace=True) # axis 0 is row, 1 is column ,index means row will removed (first row removed)
b_dt.drop(columns="age",axis=1,inplace=True)
print(b_dt.head())


"""specifing each row"""
print(b_dt.iloc[2]) # second row

print(b_dt.iloc[:,2]) #  seond colums fully

"""we can correlate every column field """

print(b_dt.corr().to_csv("predictedCorrelation.csv"))
