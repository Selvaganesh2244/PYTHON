n=int(input("Enter no.of elements:"))
even=[]
odd=[]
for i in range(n):
    num=int(input("Enter the number:"))
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:",even)
print("Odd numbers:",odd)
    
