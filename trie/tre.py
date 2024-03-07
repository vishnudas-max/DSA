class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_node = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def add(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_node = True


    def search(self,target):
        node = self.root
        for char in target:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_node
    

a=['car','bike','career','care','bivarage']
t=Trie()
for word in a:
    t.add(word)

print(t.search('bike'))
