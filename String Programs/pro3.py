def long_word(l):
    print(l)
    max = l[0]
    length = len(l[0])
    for i in l:
        if len(i) > length :
            max = i
    return max
a = input("Enter the sentence: ")
b = a.split()
c = long_word(b)
print("Longest word is ", c,"and length is ",len(c))
