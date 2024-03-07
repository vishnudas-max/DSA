class bt:
    def __init__(self,data):
        self.data =  data
        self.left = None
        self.right = None
    
    def add(self,val):
        if val == self.data:
            return
        if val < self.data:
            if self.left:
                self.left.add(val)
            else:
                self.left = bt(val)
        if val > self.data:
            if self.right:
                self.right.add(val)
            else:
                self.right = bt(val)
    
    def find_closest(self,val):

        current = self
        closest = self.data
        while self:
            if abs(val - current.data) < abs(val - closest) and current.data != val:
                closest = current.data
            if val < current.data:
                current = current.left
            elif val > current.data:
                current = current.right
            else:
                break
        return closest

        

    
    def io(self):
        a=[]
        if self.left:
            a += self.left.io()
         

        a.append(self.data)
      

        if self.right:
            a += self.right.io()
          
        
        return a
    
def buil(a):
    root = bt(a[0])

    for i in range(1,len(a)):
        root.add(a[i])

    
    return root

if __name__ == '__main__':
    a=[3,2,4,7,2,43,5,7]
    root=buil(a)
    print(root.io())
    print(root.find_closest(7))
