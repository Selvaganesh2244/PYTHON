name =input("Enter your name: ")
age = int(input("Enter your year of birth: "))
b = int(input("Enter your weight: "))
c=2023-age
if (c>=18 and b>40):
    print('1(eligible)')
else:
    print("0(not eligible)")
