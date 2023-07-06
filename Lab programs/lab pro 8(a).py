file=open("python.txt","r")
x=int(input("enter the no of lines to read:"))
for i in range(x):
    print(file.readline())
file.close()
