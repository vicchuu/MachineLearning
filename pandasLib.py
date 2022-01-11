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

print(b_dt.value_counts("age"))




