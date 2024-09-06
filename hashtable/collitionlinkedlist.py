class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next =None

class Hashtable:
    def __init__(self):
        self.size = 10
        self.table = [None for _ in range(self.size)]

    def hash(self,word):
        t=0
        for char in word:
            t += ord(char)
        return t % self.size
    
    def __setitem__(self,key,val):
        hash = self.hash(key)
        print(f"hash of {key} is {hash}")
        if self.table[hash] is None:
            self.table[hash] = Node(key,val)
        else:
            current = self.table[hash]
            while current:
                if current.key == key:
                    current.val = val
                    return
                if not current.next:
                    break
                current = current.next
            current.next = Node(key,val)

    def __getitem__(self,key):
        hash = self.hash(key)
        if self.table[hash]:
            current = self.table[hash]
            while current:
                if current.key == key:
                    return current.val
                current = current.next


h=Hashtable()
h['one']='MOnday'
h['two']='Tuesday'
h['rac'] ='APPLE'
h['car'] ='BANANA'
print(h['car'])