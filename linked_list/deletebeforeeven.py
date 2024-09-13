import random
class Node:
    def __init__(self,data=None):
        self.data =data
        self.next =None
    
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def add(self,data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next =node

        else:
            self.head = node

    def printlist(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next
    
    def deletebeforeeven(self):
        if self.head is None or self.head.next is None:
            return "There is no data or only one element"

        # Special case: If the first element's next node is even
        while self.head and self.head.next and self.head.next.data % 2 == 0:
            self.head = self.head.next  # Move the head forward if the second node is even

        prev = None
        current = self.head

        while current and current.next:
            next_node = current.next
    
            if next_node.data % 2 == 0:  # If the next node is even
                if prev is None:
                    self.head = next_node  # Remove the head if it's the first node
                else:
                    prev.next = next_node  # Skip the current node
            else:
                prev = current  # Move prev only when no deletion happens

            current = next_node  # Move current forward


    def reverse(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev


random_list = [random.randint(1, 100) for _ in range(20)]
l = LinkedList()
for i in random_list:
    l.add(i)
l.printlist()
l.deletebeforeeven()
print()
l.printlist()
print()
l.reverse()
l.printlist()