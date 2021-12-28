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
#print(X)

from sklearn.preprocessing import LabelEncoder

lencoder=LabelEncoder()
y=lencoder.fit_transform(X[:,3:4])
#print(y)

from sklearn.model_selection import train_test_split

Xtrain , Xtest,Ytrain,Ytest=train_test_split(X,y,test_size=0.1,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
Xtrain[:,1:3]=sc.fit_transform(Xtrain[:,1:3])


print (Xtrain)
print("     *****")
#print(Ytest)


