def isSorted(l):
    swapped = True
    n = len(l)
    while swapped:
        swapped = False 
        for i in range(1,n):
            if l[i] < l[i-1]:
                l[i] , l[i-1] = l[i-1] ,l[i]
                swapped = True
        if not swapped:
                break
    return l
l=[1,2,4,2,5,65,7]
k=isSorted(l)
print(f"Sorted  : {k}")