l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    p=int(input("Enter the num:"))
    l.append(p)
x=int(input("Enter the index value:"))
if x>=len(l):
    raise IndexError("Enter the correct index value")
else:
    print(l[x])
