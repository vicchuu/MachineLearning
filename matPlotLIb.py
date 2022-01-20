"""To make plots of data """
import random

import matplotlib.pyplot  as plt

"""W3e are going to plot both cos and sine curves"""
import numpy as np

x= np.linspace(0,10,10)

print(x)
y=np.cos(x)
z=np.sin(x)

# #Cosine wave
# plt.plot(x,y)
# plt.show()
#
# #sine wave
# plt.plot(x,z)
# plt.show()

#parabola
#x=np.arange(-10,10,2)
x=np.random.randint(0,40,10)
y=x**2
import re
# plt.plot(x,(x**2),scaley=True,scalex=True)
# #plt.plot(x,y, "gx")
# #plt.plot(x,y,"g.")
# plt.xlabel("x value")
# plt.ylabel("y value")
# plt.title("parabola eqtion  ")
# plt.show()
#
#
# plt.scatter(0,0,s=1000)
# plt.xlim(-4,4)
# plt.ylim(-4,4)
# plt.show()


# x=np.linspace(-5,5,60)
#
# plt.plot(x,np.cos(x),"g-")
# plt.plot(x,np.sin(x),"r--")
#
# plt.show()

"""Drawing bar plots"""
#
# bare=plt.figure() # empty figure
# ax=bare.add_axes([0,0,1,1])
# languages=["Tamil","Hindi","Telugu","Spanish","Malayalam"]
# people=[20,21,30,18,30]
# ax.pie(people,labels=languages,autopct="%0.2f%%")
# #plt.xlabel("Languages")
# #plt.ylabel("counts")
# plt.show()



"""Drawing scatter plot in empty figure"""
# x=np.linspace(-5,5,20)
# empty = plt.figure()
# ax=empty.add_axes([0,0,1,1])
# ax.scatter(x,np.sin(x),color="green")
# ax.scatter(x,np.cos(x),color="red")
# plt.show()


"""Trying 3D plot diagram"""

x=plt.figure()
s=plt.axes(projection="3d")
z=20*np.random.random(100)
y=np.sin(z)
x=np.cos(z)
s.scatter(z,y,x,c=z,cmap="Blues")
plt.show()

