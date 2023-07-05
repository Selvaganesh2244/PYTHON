numbers=[]
list=[]
print("Enter 0 to stop")
while True:
    num=int(input("Enter the number:"))
    if num==0:
        break
    numbers.append(num)
print(numbers)
numbers.sort()
print("sorted list is:")
for num in numbers:
    list.append(num)
print(list)

    
