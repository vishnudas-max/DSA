class Node:
    def __init__(self,data,next=None):
        self.data  = data
        self.next = next


class list:
    def __init__(self,head = None):
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
    
    def printer(self,first= None):
        self.fisrt =first
        first = self.head
        while first:
            print(first.data,end=' ')
            first = first.next
    def delete(self):
        current= self.head
        while current:
            runner = current
            while runner.next != None:
                if current.data == runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
    def reverse(self,head):
        if head is None:
            return
        self.reverse(head.next)
        print(head.data,end=' ')

o = list()
o.add(23)
o.add(34)
o.add(2)
o.add(23)
o.printer()
o.delete()
print('\n')
o.printer()
print('\n')
o.reverse(o.head)