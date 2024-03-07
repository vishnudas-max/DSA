class hashTable:
    def __init__(self) -> None:
        self.max=10
        self.arr = [[] for _ in range(10)]

    def hashkey(self,key):
        h= 0
        for i in key:
            h += ord(i)
        return h % self.max



    def __setitem__(self,key,value):
        hashindex = self.hashkey(key)
        
        found = False
        for idx,element in enumerate(self.arr[hashindex]):
            if len(element) == 2 and element[0] == key: # cheking if this the sae key value already exist ig exist updating it
                self.arr[hashindex][idx] = (key,value)
                found = True
                break
        if not found:
                self.arr[hashindex].append((key,value))

        return self.arr
    



    def __getitem__(self,key):
        hashindex = self.hashkey(key)
        for element in self.arr[hashindex]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h=self.hashkey(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


d= hashTable()

d['march 6']=10
d['march 6']=12
d['march 17']=100
print(d['march 17'])
del d['march 17']
print(d['march 17'])
print(d.arr)
"""
print(d.hashkey('march 6')) #out put = 9
print(d.hashkey('march 17')) #out out =9
since  march 6 and march 17 gives same hashindex when i store value in march 17 it will override the march6

d['march 6']=12
print(d['march 6']) # output 12
d['march 17'] =15
print(d['march 17']) # outputt 15
print(d['march 6']) # ooutput 15


 COLLETION HAPPENS WHEN MMULTIPLE KEY'S SHARE THE SAME HASHVALUE WE, CAN HANDLE IT USING CHAINING,LENIAR PROBING
IN CHAININ
-----------
IN CHAINING INSTED OF STORING VALUES DIRECTLY WE USSE LIST TO STORE KEY VALUE PARIRES INSIDE EACH INDEX IF
COLLISTION HAPPENDS TO THE INDEX

IN LENIAR PROBING
--------------
WHEN COLLISTION HEPPENS IT CHECK FOR THE NEXT INDEX IF IT IS FREE IT WILL STORE THE DATA IN THAT INDEX.OTHERWISE
IT WEILL CHECK FOR THE NEXT ETC


to handle collition
---------------------
first change the arr elements into a list from None
then we have to modify the setitem funtion to handle colletion
firt check if that index had elements by travelling through it
"""
