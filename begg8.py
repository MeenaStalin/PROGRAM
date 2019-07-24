key=int(input())
if(key%4==0 and key%100!=0 or key%400==0):
    print("yes")
else:
    print("no")
