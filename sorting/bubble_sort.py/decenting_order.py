def sort(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] < x[j+1]:
                x[j] , x[j+1] = x[j+1] , x[j]
    return x
a=[3,4,56,3,5,6,3,2,4,6]
k=sort(a)
print(k)