str1=input("Enter your email id:")
str2=" "
for i in str1:
    if(i=="@"):
        break
    else:
        str2+=i
str3=str2[::-1]
print("Username:",str2)
str3=str.upper(str3)
print("Password:",str2+str3)
