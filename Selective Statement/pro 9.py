print("Rating will be  \n\t1.bad \n\t2.not bad \n\t3.average \n\t4.good  \n\t5.excellent")
a = int(input("Food Rating(1-5):"))
b = int(input("Service Rating(1-5):"))
c = int(input("Ambience Rating(1-5):"))
bill = int(input("Enter Bill amount:"))

if(a==5 or a==4):
    if(b==5 or b==4 and c==5 or c==4):
        print("Tip is ",(0.1*bill))
    else:
        print("Tip is ",(0.05*bill))
else:
    if (b==5 or b==4 and c==5 or c== 4):
        print("Tip is ",(0.05*bill))
    else:
        print("Tip is ",(0.01*bill))
