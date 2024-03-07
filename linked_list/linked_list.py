# ------initialise a node-----------
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,head=None):
        self.head = head


#    ----------add a node ------------
    def add(self,data):
        new = Node(data)
        if (self.head):
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new
        else:
            self.head = new


    # -----------print a linked list---------------
    def List(self,first = None):
        self.first = first
        first = self.head
        while ( first ):
            print(first.data,end=' ')
            first = first.next
    

    # ------insert node at the begggining-------
            
    def insert(self,new=None):
        self.new = new
        newNode = Node(new)
        newNode.next = self.head
        self.head = newNode
    

    # --------insert node at the end--------------
    def insertend(self,new=None):
        self.new = new
        newNode = Node(new)
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode

    #  --------insert after a speicified node -------------
    def insertafter(self,data,x):
        self.data = data
        self.x = x
        newnode = Node(data)
        specifiednode = self.head
        while (specifiednode):
            if (specifiednode.data == x ):
                newnode.next = specifiednode.next
                specifiednode.next =newnode
            specifiednode = specifiednode.next


    # --------inser before a speicified node--------
    def insertbefore(self,data,x):
        self.data = data
        self.x = x
        prev = None
        newnode = Node(data)
        temp = self.head
        while(temp):
            if(temp.data == x):
                if prev:
                    newnode.next = prev.next
                    prev.next = newnode
                else:
                    newnode.next = self.head
                    self.head  = newnode
            prev=temp
            temp = temp.next  



    # --------------deletion of a node--------------
    def delete(self,value):
        
        temp =  self.head
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
        print('\n')



    # -----------searching of node ------------------
    
    def search(self,value):
        current = self.head
        while current:
            if current.data == value:
                print("fount")

            current = current.next



    # -------------sorting of a linked list--------------
    def sort(self):
        print('\n')
        temp = self.head
        a = []
        while temp:
            a.append(temp.data)
            temp = temp.next
        a.sort()
        new = LinkedList()
        for i in a:
            new.add(i)
        new.List()



oj = LinkedList()
oj.add(34)
oj.add(33)
oj.add(88)
oj.insert(12)

oj.insertbefore(400,33)
oj.insertafter(200,88)
oj.delete(400)
oj.List()
oj.sort()
oj.search(33)