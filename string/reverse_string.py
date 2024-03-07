def reverse(str):
    a=""
    for i in range(len(str)-1,-1,-1):
        a += str[i]
    return a
k = reverse('hello world')
print(k)
    