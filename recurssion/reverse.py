def reverse(str):
    if len(str) <=1:
        return str
    return str[-1] + reverse(str[:-1])
k=reverse('hello')
print(k)