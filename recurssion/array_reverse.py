def reverse(x):
    if len(x) <1:
        return
    print(x[-1])
    reverse(x[:-1])
reverse([1,2,34,5,6])