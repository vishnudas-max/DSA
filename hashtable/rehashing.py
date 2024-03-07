class hashtable:
    def __init__(self,max_size=5,loadfactor=.7):
        self.size=0
        self.max = max_size
        self.loadfactor=loadfactor
        self.arr = [None for _ in range(self.max)]
    def hash(self,key):
        h=0
        for i in key:
            h +=  ord(i)
        return h % self.max
    def rehash(self):
        self.max *=2
        new=[None for _ in range(self.max)]
        for i in self.arr:
            if i:
                key,value = i
                newh=self.hash(key)
                new[newh] = (key,value)
        self.arr=new

    def __setitem__(self,key,value):
        h=self.hash(key)
        if self.size / self.max >= self.loadfactor:
            self.rehash()
            h=self.hash(key)      
        self.arr[h] = (key,value)
        self.size +=1
        print(f"size {self.size}-{value}")

    def __getitem__(self,key):
        h=self.hash(key)
        return self.arr[h][1]
    
d=hashtable()
d['one']=1
d['two']=2
d['four']=5
d['three']=5
d['three']=5


print(d['two'])
print(d.arr)