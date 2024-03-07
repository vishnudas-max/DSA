# IN BUBBLE SORT EACH ELEMENT IS EVALUATED WITH IT'S IMMEDIATE NEXT ELEMENT 
def sort(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]

    return x                

a=[45,67,3,56,76,3,1,4,7,87]
p=sort(a)
print(p)