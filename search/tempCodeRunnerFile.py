def lenSearch(x,target):
              for i in range(len(x)):
                    if x[i] == target:
                          return i
              return False

s=int(input("Enter a size of the array :"))
print("Enter elements of the array :")
x=[]
for i in range(0,s):
    x.append(int(input()))
target=int(input("Enter the number to search "))

k=lenSearch(x,target)
if k:
    print(f"{target} found at position {k+1}")
else:
       print('not found')