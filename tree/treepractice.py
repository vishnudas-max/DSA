class tr:
    def __init__(self,data):
        self.data =data
        self.children = []
        self.parent = None
    
    def add(self,child):
        child.parent = self
        self.children.append(child)
    
    def lvl(self):
        h=0
        k=self
        while k.parent:
            h += 1
            k = k.parent
        
        return h
            

    def printer(self):
        space = ' ' * self.lvl() * 2
        prefix = space + '|___' if self.parent else ""
        print(prefix  + self.data)
        
        if self.children:
            for i in self.children:
                i.printer()
        


def build_product_tree():

    root = tr('Electornics ')


    # creatig laptop node-
    laptop =  tr('laptop')

    # adding childes to laptop--
    laptop.add(tr('asus'))
    laptop.add(tr('mac'))
    laptop.add(tr('hp'))

    # creating mobbile node-
    mobile = tr('mobile')

    # adding child to mobile-
    mobile.add(tr('redmi'))
    iphone=tr('Iphone')
    iphone.add(tr('iphone 12 pro'))
    iphone.add(tr('iphoe 13 pro max'))
    iphone.add(tr('iphone 15'))
    mobile.add(iphone)
    mobile.add(tr('samsung'))

    # adding child to root node electronics-
    root.add(laptop)
    root.add(mobile)

    root.printer()
    return root



if __name__ == '__main__':
    build_product_tree()
    pass