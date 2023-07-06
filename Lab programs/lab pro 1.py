def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def palindrome(n):
    return str(n) == str(n)[::-1]

def count_digits(n):
    return len(str(n))

num = int(input("Enter the number: "))

if (num%2==1):  
    fact = fact(num)
    digits = count_digits(fact)
    print("Factorial of", num, "is", fact)
    print("Number of digits in the factorial:", digits)
else:  
    if palindrome(num):
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")
