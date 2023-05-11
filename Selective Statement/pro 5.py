a =int(input("enter side 1:"))
b =int(input("enter side 2:"))
c =int(input("enter side 3:"))
if(a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2):
    print("1")
else:
    print("0")
