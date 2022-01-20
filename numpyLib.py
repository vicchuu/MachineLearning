"""Numerical python make easier and speed up arithmethim operations"""
import numpy as np


from time import process_time

lis= [i for i in range(10000) ]

strt=process_time()
lis=[i+5 for i in lis]
endTime=process_time()

print("Normal time :",strt,endTime)
print("Total Normal :",((endTime-strt)))

print("**** Numpy comp")

NParr=np.array([i for i in range(10000)])
strt=process_time()
NParr+=5
endTime=process_time()
print("NUM time :",strt,endTime)
print("tot time taken in NUMpy :",float(endTime-strt))

print(NParr) # no comma is mentioned
print(type(NParr))
""" not mentined as list it will be as numpy.ndarray."""


"""Shape"""
print(NParr.shape , NParr.size) # size result will be in m*n

a=np.array([(1,2,3),(9,8)],dtype="object") # if we give diff length , we need to mention dtype

print(a.shape )

"""intializing all value as zeros"""
b=np.zeros((2,3),dtype="int")

print(b)

"""Same for all value as 1"""
c=np.ones((2,2),dtype=int)
print(c)


"""If we need to fill particular value """
d=np.full((2,3),6,dtype=int)
print(d)

"""We can create identity matrix"""

e=np.eye(3 )
print(e)


"""To create random matrixes """
f=np.random.random(10)  # it will create in only 0.0 to 1.0 float
g=np.random.randint(1,20,(3,2))

print(g)


"""If we need evenly speed values """
h=np.linspace(20,100,2,dtype=int) # need to specify no of values
print(h)

"""If we need line gap"""
i=np.arange(10,200,23) # need to specify the gap betwn , intervals

print(i)


"""Converting a normal list to np array"""
arr1=[1,2,3,4,5,6]

arr2=np.asarray(arr1)

"""We can find dimension"""

print(g.ndim)
print(g.size)


"""We can add directly with using nparray , normal array will concat if we use + optr"""
a1=np.array([1,2,3,4,5])
a2=np.array([99,98,97,96,95])
print(a1+a2)   # we can do other arithmetic operation



"""other wise we can do with use of method add"""
c1=[1,2,3]
c2=[5,6,7]

print(np.add(c1,c2))
print(np.subtract(c1,c2))
print(np.divide(c1,c2))
print(np.power(c1,c2))
print(np.multiply(c1,c2))


"""We can transpose matrix """
q1=[[(1,2,3),(9,8,7)]]
#print(np.transpose(q1))
#print(np.asarray(q1).T)

"""We can reshape an array""" #2*3 = 3*2

print(np.asarray(q1).reshape(len(q1[:]),len(q1)))

