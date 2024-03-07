
def replace(s):
    l=len(s)
    new_string = ""
    for i in range(l):
        if s[i] == 'x':
            ac=ord(s[i])
            c = chr(ac+2)
            new_string += c
            continue
        elif s[i] == 'y':
            ac=ord(s[i])
            c = chr(ac+1)
            new_string += c
            continue           
        elif s[i] == 'z':
            new_string += s[i]
        else:
            ac=ord(s[i])
            c = chr(ac+3)
            new_string += c
    return new_string

string = input("Enter a String ")
print(f"String before convertig is = {string}")
string.lower()
a=replace(string)
print(a)