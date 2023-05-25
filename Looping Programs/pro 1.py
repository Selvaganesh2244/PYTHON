even=0
odd=0
start=int(input("enter staring number:"))
end=int(input("enter ending number:"))
for i in range(start,end+1):
     if(i%2==0):
          even=even+1
     else:
          odd=odd+1
print("even:",even)
print("odd:",odd)
          
