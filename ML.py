import numpy as np
import matplotlib
import pandas as ps


readCSV=ps.read_csv("Data.csv")
X=readCSV.iloc[:,:].values
#print(X)

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(X)


