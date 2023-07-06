l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    p=int(input("Enter the num:"))
    l.append(p)
try:
    x=int(input("Enter the index value:"))
    print(l[x])
except:
    print("index not present,the last index value is:",len(l)-1)
