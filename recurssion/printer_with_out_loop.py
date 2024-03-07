def printer(n):
    if n == 0:
        return 
    print(n)
    printer(n-1)
    print(f'{n} hello')

printer(10)