class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next = None
    
class link:
    def __init__(self,head=None):
        self.head=head
    
    def add(self,data):
        new=Node(data)
        if self.head:
            temp= self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new
        self.head = new
    
    def addf(self,data)
        new = Node(data)
        if self.head:
            new.next =self.head
            self.head = new