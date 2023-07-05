square_set = {x**2 for x in range(1, 31)}

divisible_by_3 = [x for x in range(1, 31) if x % 3 == 0]

new_set = square_set - set(divisible_by_3)

print("Square Set:", square_set)
print("Divisible by 3 List:", divisible_by_3)
print("New Set:", new_set)
