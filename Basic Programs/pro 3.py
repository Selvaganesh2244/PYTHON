a=int(input("Enter a temperature in degree celsius:"))
b=int(input("Enter a wind speed kilometers/hour:"))
c=13.12+(0.6215*a-11.37*b**0.16)+(0.3965*a*b**0.16)
print("the calculated a wind speed of chill index in celsius:",int(round(c,0)))
