def binarySearch(l,target):
    left = 0 
    right = len(l) -1

    while left <= right:
        mid = ( left + right ) // 2
        if l[mid] == target:
            return mid+1
        elif target < l[mid] :
            right = mid - 1
        else:
            left = mid + 1
    return False
a=[1, 3, 4, 5, 6, 9, 11, 15, 18, 21, 25]
a.sort
target=15
k=binarySearch(a,target)
if k:
    print(f"{target} found at position {k}")
else:
    print(f"{target} not found")