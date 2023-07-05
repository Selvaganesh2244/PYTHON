n=0
e=0
o=0
while n!=-1:
    n=int(input("Enter a number:"))
    if(n%2==0):
        e=e+1
    else:
        o=o+1
print("even no:",e)
print("odd no:",o-1)
