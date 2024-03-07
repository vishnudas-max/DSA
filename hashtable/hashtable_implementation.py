#IN PYTHON A HASH TABLE IS IMPLEMENTED AS A DICTIONARY , A HASH TABLE IS A DATASTRUCTURE THAT STORES KEY VALUE PAIRES,
#IT USES A HASH FUNCTION TO COMPURE AN INDEX IN  TO AN ARRAY OF BUCKETS OR SLOTES FROM WHICH THE DESIRED VALUE CAN BE FOUND 
class hashTalble:
    def __init__(self):
        self.max = 100
        self.arr = [None for _ in range(self.max)]

    def gethash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.max
    def add(self,key,val):
        hashindex=self.gethash(key)
        self.arr[hashindex] = val

    def get(self,key):
        hasindex = self.gethash(key)
        return self.arr[hasindex]

    def delete(self,key):
        hashindext = self.gethash(key)
        del self.arr[hashindext] 


d=hashTalble()
d.gethash('visnu')
d.add('monday',1)
d.add('sunday',2)
d.add('friday',34)
print(d.get('monday'))
d.delete('monday')
print(d.get('monday'))
