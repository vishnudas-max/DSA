def binarySearch(x, target):
    left = 0
    right = len(x) - 1

    while left <= right:
        mid = (left + right) // 2

        if x[mid] == target:
            return mid
        elif target < x[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False

s = int(input("Enter the size of the array: "))
print("Enter elements of the array:")
x = [int(input()) for _ in range(s)]

x.sort()

target = int(input("Enter the number to search: "))
print(x)

position = binarySearch(x, target)
if position is not False:
    print(f"Found at position {position}")
else:
    print("Not found")
