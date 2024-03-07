class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    



    def add_child(self,child):
        child.parent = self
        self.children.append(child)




    def get_level(self):
        level=0
        h=self
        while h:
            level +=1
            h=h.parent
        return level
    



    def printTree(self):
        spaces =' ' * self.get_level() * 3
        prefix = spaces + '|___' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for i in self.children:
                i.printTree()




def build_product_tree():

    root = TreeNode('Electornics ')


    # creatig laptop node-
    laptop =  TreeNode('laptop')

    # adding childes to laptop--
    laptop.add_child(TreeNode('asus'))
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('hp'))

    # creating mobbile node-
    mobile = TreeNode('mobile')

    # adding child to mobile-
    mobile.add_child(TreeNode('redmi'))
    iphone=TreeNode('Iphone')
    iphone.add_child(TreeNode('iphone 12 pro'))
    iphone.add_child(TreeNode('iphoe 13 pro max'))
    iphone.add_child(TreeNode('iphone 15'))
    mobile.add_child(iphone)
    mobile.add_child(TreeNode('samsung'))

    # adding child to root node electronics-
    root.add_child(laptop)
    root.add_child(mobile)

    root.printTree()
    return root



if __name__ == '__main__':
    build_product_tree()
    pass