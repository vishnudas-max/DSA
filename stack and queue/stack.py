# statck implementation using list
my_list=['sunday','monday','tuesday','wednessday','thursday','friday','saturday']
stack = []

# addin elements into a stack
for i in range(len(my_list)):
    stack.append(my_list[i])
    print(stack)
    

# update data in a stack
print('After updation')
def update(data,value):
    # for i in range(len(stack)):
    #     if stack[i] == data:
    #         stack[i] = value
    #         break
	#  or-=
    ind=stack.index(data)
    print(ind)
    stack[ind] = value
    return stack

print(update('monday','Monday'))


# print('After deletion')
# # # removing elements fromm the stack
# for i in range(len(stack)):
#     stack.pop()
#     print(stack)
    
# STACK USING ARRAY---
import array as arr
stack = arr.array('i',[2,3,4,4,4,5,5,6,78,8])


print('print stack')
def printstack():
    for i in stack:
        print(i,end=' ')
printstack()

# inserting element into stack-
print('insertion')
def push(data):
    stack.append(data)
    return stack
print(push(200))

# deletion fro th stack
print('deletion')
def pop():
    stack.pop()
    printstack()


pop()


# updating element in a stack-
print('updating')
def update(data,value):
    ind = stack.index(data)
    stack[ind] = value
    printstack()
    
update(5,100)


# -------------------------IMPLEMENT STACK USING DEQUE MEHTOD---------------
from collections import deque
print('\n')
print('stack imlementation using deque')
stack = deque() #Thsi will create a empty stack
a=[2,3,4,5,3,2,4,6,7,8]
print(stack)


# insertion-
print('insertion')
for i in range(len(a)):
    stack.append(a[i])
    print(stack)
    
# deletion -
print('deletion')
for i in range(len(stack)):
    stack.pop()
    print(stack)



# sorting-

def sort(stack):
    a=[]
    for i in range(len(stack)):
        temp = stack.pop()
        a.append(temp)
    a.sort()
    for i in range(len(a)):
        stack.append(a[i])
    return stack

stack=deque([3,5,5,2,34,6,8,9,9,4])
print(f"Before sorting {stack}")
print("After sorting")
print(sort(stack))