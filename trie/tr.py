class TreeNode:
    def __init__(self):
        self.children = {}
        self.end_of_the_word= False

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] =TreeNode()
            node = node.children[char]
        node.end_of_the_word = True
    def search(self,target):
        node = self.root
        for char in target:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_the_word


    

t=Trie()
words=['car','bike','carpender','biker']
for word in words:
    t.insert(word)
print(t.root.children)
print(t.search('car'))