def encode_string(string):
    encoded_list=[]
    for i in string:
        encoded_list.append(ord(i))
    return encoded_list
str=input("Enter the string:")
result=encode_string(str)
print("Encode the list - ",result)
