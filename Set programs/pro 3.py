vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
str=input("Enter a string :")
str=str.lower()
for char in str:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:", count)
