a='python'
b="python"
print(a)
print(b)

# ----mulitline string-
a ="""python
     is 
     a 
     interpreted 
     language"""
print(a)

# slicing in string---
a="python is an interpreted language !"
print(a[:5])
print(a[5:])

# [start:stop:skip]--
print(a[::2])


# -----------blank space is also considered as a string--
print(a[6])
print(a[5])

# ---reverse---
print(a[::-1])
print(a[-5:-1])


# ----------------------------STRING MEHTHODS-----------------

name = "vishnu"
print(name.capitalize())

# to find the count of character--
print(name.count('i'))

# to find the position of a character -
print(name.find('i'))


# return true if all are alphanumeric-
print(name.isalnum())

# return true if all are alpha
print(name.isalpha())

# return true if it is lower
print(name.islower())

# return true if it is upper
print(name.isupper())

# to change to lower
print(name.upper())

# to change to lower
print(name.lower())

# to replace a character-
print(name.replace('i','!'))

a='hai vishnu'
print(a.strip())
print(a.split(' '))


# -string interpolation---
a='python'
b='brototype'
c="you can learn %s from %s"%(a,b)
print(c)

# or--
print(f"You can learn {a} from {b}")


# or---
print("hai {b}".format(b='vishnu'))