def generate_primes(start, end):
    primes = set()
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    break
                else:
                    primes.add(num)
    return primes

def generate_divisible_by_5(start,end):
    divisible_by_5 = set()
    for num in range(start,end+1):
        if num % 5 == 0:
            divisible_by_5.add(num)
    return divisible_by_5

prime_numbers = generate_primes(1, 50)
print("prime numbers=",prime_numbers)
divisible_by_5 = generate_divisible_by_5(1,50)
print("numbers divide by 5",divisible_by_5)

union_set = prime_numbers.union(divisible_by_5)
intersection_set = prime_numbers.intersection(divisible_by_5)
difference_set = prime_numbers.difference(divisible_by_5)
symmetric_difference_set = prime_numbers.symmetric_difference(divisible_by_5)


print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
