
x=[1,2,34,[3,4,5],[5,6,7]]
c=[]
def flttern(x):
    for i in x:
        if isinstance(i,list):
             flttern(i)
        else:
            c.append(i)
    return c
d=flttern(x)
print(d)