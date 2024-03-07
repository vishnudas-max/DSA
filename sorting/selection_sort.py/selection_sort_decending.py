def selection_sort(l):
        for i in range(0,len(l)-1):
                maxpos=i
                for j in range(i,len(l)):
                        if l[j] > l[maxpos]:
                                maxpos = j
                if l[maxpos] > l[i]:
                        l[maxpos] , l[i] = l[i] , l[maxpos]

        return l




le=int(input('Enter the size of the array:'))
l=[ int(input("Enter the element :")) for _ in range(le)]
print(f"Before sorting : {l}")
k=selection_sort(l)
print(f"After soring : {k}")