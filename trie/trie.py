class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
words = ["apple", "app", "ape", "dog", "cat"]
for word in words:
    trie.insert(word)

print(trie.search("app"))  # True
print(trie.search("dog"))  # True
print(trie.search("cat"))  # True
print(trie.search("ape"))  # True
print(trie.search("apple"))  # True
print(trie.search("banana"))  # False

print(trie.starts_with("do"))  # True
print(trie.starts_with("ba"))  # False
