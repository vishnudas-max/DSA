class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class List:
    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):
        self.data = data
        new = Node(data)

        if self.head:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new
        else:
            self.head = new

    def printlist(self,first=None):
        first = self.head
        while first:
            print(first.data)
            first = first.next
    
    def reverse(self,first):

        if first is None:
            return
        
        self.reverse(first.next)
        print(first.data)

    def insert(self,x,value):
        temp =self.head
        newvalue = Node(value)
        while temp:
            if temp.data == x:
                newvalue.next = temp.next
                temp.next = newvalue
            temp = temp.next

        
    
o = List()
o.add(3)
o.add(5)
o.add(45)
o.printlist()
print('\n')
o.reverse(o.head)
