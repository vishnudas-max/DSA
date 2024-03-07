from collections import deque
l=[1,2,3,4,5,67,8,8]
stack=deque()
for i in l:
    stack.append(i)
print(stack)

temp=[]
for i in range(len(stack)):
    d=stack.pop()
    temp.append(d)
print(temp)
temp.sort()
for i in temp:
    stack.append(i)

print(f"after soring {stack}")