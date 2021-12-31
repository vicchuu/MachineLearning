
"""importing lib
"""
import pandas as ps
import numpy as np

"""adding data set"""

dataset=ps.read_csv("50_Startups.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values


print(X)