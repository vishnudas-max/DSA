class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,data):

        # checking if current data is already in the tree-
        if data == self.data:
            return
        
        # adding node on the left side of th current node if the data is less than the current node-
        if data < self.data:
            # checking if left node has data-
            if self.left:
                # calling the addfuction from the leftnode-
                self.left.add_child(data)
            else:
                # adding node data in the leftnode-
                self.left = BST(data)

        # adding node on the right side of the current node if the data is greater than the currrent node-
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

        
    
    # travensting through the binary search tree-
    def in_order_traversal(self):
        elements = []

        # visting left node--
        if self.left:
            # calling the in order traversal recursively and adding the list of values genarated after breaking recustion -
            # elements -
            elements += self.left.in_order_traversal()

        # visiting base node--
        elements.append(self.data)


        # visiting right node-
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self,val):
        
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            

    def find_min(self):
        
        if not self.left:
            return self.data
        if self.left:
            return self.left.find_min()
    
    def find_max(self):
        if not self.right:
            return self.data
        if self.right:
            return self.right.find_max()
        
    def sum(self):
        sum =0
        if self.left:
            sum += self.left.sum()
        sum += self.data
        if self.right:
            sum += self.right.sum()
        return sum
    
    def post_order_traversal(self):
        elements= []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements
    

    def pre_order_traversal(self):
        elements =[]
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements


    def delete(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
                
        
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
                
        else:
            if self.left == None and self.right == None:
                return None

            if self.left == None:
                return self.right
                

            if self.right == None:
                return None
            
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        
        return self
    
    def bfs(self):
        queue=[self]
        while queue:
            s =queue.pop(0)
            print(s.data,end=' ')
            if s.left:
                queue.append(s.left)
            if s.right:
                queue.append(s.right)

def build_tree(elements):

    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root



if __name__ == '__main__':
    elements = [76,3,67,2,90,30,2]
    root=build_tree(elements)
    print(root.in_order_traversal())
    print(root.search(222))
    print(root.find_min())
    print(root.find_max())
    print(root.sum())
    print(root.post_order_traversal())
    print(root.pre_order_traversal())

    root.delete(8787)
    print(f"after deleting 3 from the tree {root.in_order_traversal()}")

    root.bfs()
