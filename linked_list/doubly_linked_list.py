class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doublyList:
    def __init__(self,head=None):
        self.head = None
    
    def add(self,data):
        
        new = Node(data)
        if self.head:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new
            new.prev = temp
        else:
            self.head = new
        
    def printList(self,first=None):
        self.first = first
        first = self.head
        while first:
            print(first.data)
            print(f"prev ={first.prev}")
            print(f"next ={first.next}")
            first = first.next
        

o = doublyList()
o.add(23)
o.add(44)
o.add(89)
o.printList()