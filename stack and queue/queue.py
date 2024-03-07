# -----------QUEUE IMPLEMENTATION USING LIST-------------------------
queue=[]
def enqueue(data):
    queue.append(data)
    print(queue)


enqueue(12)
enqueue(13)
enqueue(34)

def dequeue():
    queue.pop(0)
    print(queue)
print('dequeue')
dequeue()

def update(data,value):
    ind=queue.index(data)
    queue[ind] =value
    print(queue)

print('update')
update(13,100)


# QUEUE USING ARRAY ----------------
import array as a
queue=a.array('i',[4,23,4,6,78,9,90])
def read():
    for i in queue:
        print(i,end=' ')

print('reading')
read()

# queue using deque------------------
from collections import deque
print('\n')
print('queue using deque')
queue=deque()
def insert(data):
    queue.append(data)
    print(queue)
insert(12)
insert(1)
insert(23)
print('deque')
def dequeue():
    queue.popleft()
    print(queue)

dequeue()
dequeue()
dequeue()