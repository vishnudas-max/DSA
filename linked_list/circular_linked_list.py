class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class circularList:
    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):

        new = Node(data)

        if self.head:
            
            last= self.head
            while last.next != self.head:

                 last = last.next
            new.next = self.head
            last.next = new
        else:
            self.head = new
            new.next = self.head
    

    def printList(self,first=None):
        self.first=first
        first = self.head
        while(first):
            print(first.data)
            if first.next == self.head:
                break
            first = first.next


o = circularList()
o.add(12)
o.add(23)
o.add(12)
o.printList()
