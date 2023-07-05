def recur_fibo():
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-1))
    nterms=int(input("Enter number:"))
    s=0
    if nterms<=0:
        print("please enter a positive integer")
    else:
        for i in range(nterms):
            s=recur_fibo(1)
        print(s)
