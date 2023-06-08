start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
for i in range(start,end+1):
     if(i>1):
          for j in range(2,i):
               if(j%i==0):
                    print(i)
