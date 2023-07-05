import math
def fact_list(numbers):
    result=[]
    for num in numbers:
        factorial=math.factorial(num)
        result.append(factorial)
    return result
numbers=[]
for i in range(5):
    number=int(input("Enter the number:"))
    numbers.append(number)
fact_list=fact_list(numbers)
print(fact_list)
