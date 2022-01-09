

import pandas as ps
import numpy as np


dataset=ps.read_csv("Position_Salaries.csv")
#dataset=dataset.fillna(dataset.median())
print(dataset.shape)

X=dataset["Level"]
Y=dataset["Salary"].fillna(dataset["Salary"].median())
print(Y)

print(dataset.isnull().sum())

print("@@@@@")

#Tips: if the data is skewed then its not recommended to fill data in mean ,  median or mode is good



#Encoding NA bu mode
