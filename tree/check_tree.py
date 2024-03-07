class tr:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def io(self):
        e= []
        if self.left:
            e += self.left.io()
        e.append(self.data)

        if self.right:
            e += self.right.io()
        
        return e
    
    def check(self):
        a=self.io()
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True


    
def build():
    root = tr(5)
    root.left = tr(3)
    root.right = tr(6)
   
    return root
if __name__ == '__main__':
    root = build()
    print(root.io())
    print(root.check())