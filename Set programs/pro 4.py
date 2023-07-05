List1 = [10, 45, 34, 20, 11]
List2 = [11, 25, 45, 20]
List3 = [20, 25, 11, 14, 45, 65]

set1 = set(List1)
set2 = set(List2)
set3 = set(List3)

common_elements = set1.intersection(set2, set3)

print("Common elements:", common_elements)
