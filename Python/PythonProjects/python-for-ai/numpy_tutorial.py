import numpy as np

values=[10.3,34,56.7,78.0,45]
Convert=np.array(values)
print(Convert)
print(Convert+20)

# Creating an array
arr=np.array([1,2,3])
print(arr)
print(type(arr))

# 2-D array
arr1=np.array([[4,5,6]])
print(arr1)
print(type(arr1))

arr2=np.array([1,2,3],dtype=float)
print(arr2)
print(type(arr2))

arr3=np.array([1,2,3],dtype=str)
print(arr3)
print(type(arr3))
print(len(arr3))

b=np.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))
print(len(b))

c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(type(c))
print(len(c))

# Get dimensions of a numpy array
print(b.ndim)
print(c.ndim)
print(arr3.ndim)

d=np.array([[[1,2,3],[6,7,8]]])
print(d.ndim)

a=np.array([[1,2,3]])
print(a)
print(len(a))
# Get the shape of a numpy array
print(a.shape)

print(b.shape)
print(c.shape)
print(d.shape)
# Get the data type
print(b.dtype)
print(c.dtype)

# Accessing or changing specific elements, rows and columns etc
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a.ndim)
print(a.shape)
# Get the specific element at [r,c]
print(a[0][3])
print(a[1][4])

# Get a specific row from a numpy array
print(a[0,:]) # print first row
print(a[1,:]) # print second row

# Get a specific column from a numpy array
print(a[:,0]) # first column
print(a[:,1]) # print second column
print(a[:,6]) # print seventh column

# Changing elements
a[1][0]=8
print(a)
a[1][2]=1
print(a)

# Zeros/ Ones method in Numpy
np.zeros((3,3)) # gives a 3*3 matrix with all values as 0.
np.ones((2,4)) # gives a 2*4 matrix with all values as 1.
# changing the data type of a numpy array
np.ones((2,2),dtype='int32')
np.zeros((4,3),dtype='int')
np.ones((3,4),dtype='int')
np.ones((2,3),dtype='str')
np.zeros((2,2),dtype='str')

# Filling all the values in an array with the same number
np.full((3,2),5,dtype='int')
np.full((2,4),13,dtype='float')
var=8
np.full((3,3),var,dtype='int')

# Create an array of random numbers
np.random.rand(4,4)

# must specify the range eg: here 1 to 5 or else error
np.random.randint(1,5,size=(3,3))
np.random.randint(-4,1,size=(3,4))

np.identity(5)
np.identity(3,dtype='int')


# Questions
# Extract all the first 3 rows of the last 5 columns in the given numpy 2D array a?
a=np.array([[1,2,3,4,5,6],
           [10,20,30,40,50,60],
           [11,21,31,41,51,61],
           [13,24,34,44,54,64] 
            ])

print(a[:3,-5:])
print(a[0:3,-5:])


# Q -2 
# Given a positive number 'n' greater than 2, create a numpy array of size (n×n) with all zeros and ones such that the ones make a shape of "+"
# input : 3
# output : [[0,1,0],[1,1,1],[0,1,0]]
# To form such a + shape ones, the middle row and columns should have all values as 1.
n=int(input('Enter an integer greater than 2 : '))
z=np.zeros((n,n),dtype='int')
print(z)
# Make the middle row and columns all 1's
z[n//2,:]=1
z[:,n//2]=1
print(z)

# Arithmetic operations with NumPy - Maths + Statistics
p=np.array([1,2,3,4,5])
print(p+2)
print(p*3)
print(p**2)
p.min()
np.min(p)
p.max()
np.max(p)
p.mean()
np.mean(p)

q=np.array([[1,-6,3],[4,9,6]])
print(q)
np.max(q)
q.max()
np.max(q,axis=0)
np.max(q,axis=1)
np.min(q)
q.min()
np.min(q,axis=0)
np.min(q,axis=1)
q.ndim
q.mean()
np.mean(q)
q.sum()
np.sum(q)
np.sum(q,axis=0)
np.sum(q,axis=1)








