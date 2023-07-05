l1 = [1,1,1,2,2,3,4,4,5,6,6,7,8,9]
new_list = []
for i in l1:
    if i not in new_list:
        new_list.append(i)

print(new_list)
