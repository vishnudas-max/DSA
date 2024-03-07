import numpy as np
# creating array---
x=list(range(0,100))
arr1=np.array(x)
for i in arr1:
    print(arr1[i],end=' ')

# array with zeros--
print(np.zeros((2,2)))

# array of ones--
print(np.ones((2,2)))

# array of constants---
print(np.full((2,2),8))

# identity matrix--
print(np.eye(3))

# array of random values--
print(np.random.random((2,2)))
# mulitidiamensitonal array --

print(np.array([1]))

print(np.array([1,1]))

print(np.array([[1,1],[2,2]]))

# or

print(np.array([1,12,2,3,4,4,5,5,5,6,67,],ndmin=3))

# to find the diamention---
print(arr1.ndim)

# to delete------
print('before deletion')
print(arr1)
p=np.delete(arr1,0)
print('after deletion')
print(p)


# searching---
position=np.where(arr1 == 10)
print(position)
print(arr1[position])


# sorting-----
print(np.sort(arr1))


# mathematical oparations--------
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[3,4],[5,6]])
print(arr1.ndim)
print(arr1)
print(arr2)

# additon--
print('sum =')
print(np.add(arr1,arr2))

# substraction--
print('difference =')
print(np.subtract(arr1,arr2))

# multiplication----
print('product is =')
print(np.multiply(arr1,arr2))

# division----
print('quaitnt  =')
print(np.divide(arr2,arr1))

# squre root ---
print('squre root =')
print(np.sqrt(arr1))

# transpose--
print('transpose =')
print(np.transpose(arr1)) 


# to flatten------
flatted_array=arr1.flatten()
print(flatted_array)

ar=np.array([[1,2,34],[3,4,5]])
print(ar.flatten())

print('a')


b=[[1,2,34],[3,4,5]]
a=[]
def flate(b):
    for i in b:
        if isinstance(i,list):
            flate(i)
        else:
            a.append(i)
    return a
print(flate(b))