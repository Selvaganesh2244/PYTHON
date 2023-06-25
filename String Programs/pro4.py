str=(input("Enter string: "))
l=len(str)
if (l%5==0):
    a=str[::-1]
    print(a.upper())
else:
    print("Given string length is not a multiple of 5")
