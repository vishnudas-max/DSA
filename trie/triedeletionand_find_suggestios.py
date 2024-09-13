class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self,word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.end_of_word = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.end_of_word
    
    def delete(self,word):
        def _delete(node,word,index):
            if not node:
                return False
            if len(word) == index:
                if node.end_of_word:
                    node.end_of_word = False
                
                return len(node.children) == 0
            
            char = word[index]

            if char in node.children:
                can_delete_child = _delete(node.children[char],word,index + 1)

                if can_delete_child:
                    del node.chidren[char]

                    return len(node.children) == 0 and not node.end_of_word

            return False
        
        _delete(self.root,word,0)


    def dfs(self,node,prefix,suggestions):
        if node.end_of_word:
            suggestions.append(prefix)
        for char,child in node.children.items():
            self.dfs(child,prefix + char,suggestions)

        return suggestions

    def find_suggestions(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions=[]
        self.dfs(node,prefix,suggestions)
        return suggestions

t=Trie()
t.insert('vishnu')
t.insert('vishnudas')
t.insert('vishu')
t.insert('vipin')
t.insert('bank')
t.insert('banker')
print(t.search('bank'))
t.delete('bank')
print(t.search('banker'))
print(t.find_suggestions('vis'))