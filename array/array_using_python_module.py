# creation of array using python array module-
import array as a
x=list(range(0,100,2))
# creation--Syntax = array.array.('type',array)
arr1=a.array('i',x)
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')

# insertion_at index
arr1.insert(1,20)
print('\n')
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')
# insertion at end--
print('\n')
arr1.append(200)
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')


# deletion---
# deleting element at first index--
print('\n')
arr1.pop(1)
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')

print('\n')
arr1.remove(0)
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')


# slicing-----------
print('\n')
print(arr1[0:10])
k=arr1[0:10]

# reversing--
print('\n')
print(k[::-1])