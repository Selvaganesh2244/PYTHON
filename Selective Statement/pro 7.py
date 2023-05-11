a=int(input("Enter your salary: "))
b=int(input("Enter your year of service: "))

if(b>10):
    c=a+(0.1*a)
    print("your bonus is: ",c)
elif(b>6 and b<=10):
    c = a+(0.08*a)
    print("your bonus is: ", c)
elif(b<6):
    c = a+(0.05 *a)
    print("your bonus is: ", c)
else:
    print("no bonus for u ")
