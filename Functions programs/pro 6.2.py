def series(n,x):
    d=2
    s=0
    for i in range(0,n):
        s=s+(x/d)
        d=d*2
        print(s)
num=int(input("N="))
x=int(input("x="))
series(num,x)
