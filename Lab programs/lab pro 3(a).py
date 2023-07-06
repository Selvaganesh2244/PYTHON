l=[]
n=int(input("Enter the no of elements:"))
for i in range(n):
    p=int(input("Enter the number:"))
    l.append(p)
print(l)
r=int(input("Enter the element to search:"))
print("Positive index:")
for j in range(len(l)):
    if(l[j]==r):
        print(j,end=' ')
print()
print("Negative index:")
for k in range(-len(l),0):
    if(l[k]==r):
        print(k,end=' ')
