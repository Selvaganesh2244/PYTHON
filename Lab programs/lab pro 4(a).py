t=[]
n=int(input("Enter the no. of elements in tuple :"))
for i in range(n):
    p=input("Enter the element of tuple:")
    t.append(p)
t=tuple(t)
print(t)
s=""
for i in t:
    s=s+i
print(s)
