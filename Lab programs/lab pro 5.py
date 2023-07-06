a={1,2,3,4}
b={1,2,3}
c=0
for i in b:
    if i in a:
        c=c+1
if c==len(b):
    print("b is a subset of a")
