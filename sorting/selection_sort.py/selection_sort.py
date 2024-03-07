def selection_sort(l):
    for i in range(0,len(l)-1):
        minpos = i
        for j in range(i,len(l)):
            if l[j] < l[minpos]:
                minpos = j
        l[i] ,l[minpos] = l[minpos] ,l[i]
    
    return l


l=[5,23,4,6,2,5,212,34,0]
k=selection_sort(l)
print(k)