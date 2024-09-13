class Tree:
    def __init__(self,data=None):
        self.data =data
        self.left =None
        self.right =None

    def add(self,data):
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Tree(data)
        if data > self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right = Tree(data)

    
    def inorder(self):
        p=[]
        if self.left:
            p += self.left.inorder()

        p.append(self.data)

        if self.right:
            p += self.right.inorder()

        return p
    
    def bfs(self):
        queue =[self]
        while queue:
            s= queue.pop(0)
            print(s.data,end=' ')
            if s.left:
                queue.append(s.left)
            if s.right:
                queue.append(s.right)


    def min(self):
        if not self.left:
            return self.data
        else:
            return self.left.min()
        
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min = self.right.min()
            print(min)
            self.right = self.right.delete(min)
        return self
    
def build(l):
    root = Tree(l[0])
    for i in range(1,len(l)):
        root.add(l[i])

    return root

if __name__ == '__main__':
    l=[1,2,43,54,54,12,4,645,32]
    root = build(l)
    print(root.min())
    print(root.inorder())
    root=root.delete(1)
    print(root.inorder())
            