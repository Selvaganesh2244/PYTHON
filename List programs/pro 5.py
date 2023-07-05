n=int(input("Enter the no.of words:"))
word_list=[]
for i in range(n):
    word=input("Enter a word:")
    word_list.append(word)
for word in word_list:
    print(word,"-",len(word))
long_word=max(word_list,key=len)
print("longest word is:",long_word)
