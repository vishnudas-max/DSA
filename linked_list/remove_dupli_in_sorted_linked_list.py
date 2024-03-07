class Node:
    def __init__(self,data,next=None):
        self.next = next
        self.data = data
class List:
    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):
        new = Node(data)
        if self.head:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next =new
        else:
            self.head = new

    def printer(self,first=None):
        self.first = first
        first = self.head
        while first:
            print(first.data,end=" ")
            first = first.next    


    def delete(self):
        curent = self.head
        val =curent.data
        while curent.next:
            if curent.data == curent.next.data:
                curent.next = curent.next.next
            else:
                curent = curent.next
        self.printer()
        


        
o =List()
o.add(1)
o.add(2)
o.add(2)
o.add(3)
o.add(4)
o.add(5)
o.add(5)
print('\n')
o.printer()
print('\n')
o.delete()


