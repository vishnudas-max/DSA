
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] < arr[j] and j > 0:
            arr[j] , arr[j-1] =arr[j-1] ,arr[j]
            j -= 1
    return arr

d=[1,3,4,1,4,6,2,5,64,6,456,0,2,4556,34]
print(insertion_sort(d))
