class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):
        new = Node(data)
        if self.head:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new
        else:
            self.head = new

    def printer(self,first=None):
        self.first = first
        first = self.head
        while first:
            print(first.data,end=' ')
            first = first.next

    def convert(self,x):
        new = LinkedList()
        if isinstance(x, int):
            new.add(x)
        else:
            for i in x:
                new.add(i)
        new.printer()

o = LinkedList()
o.convert(22)