ket=int(input())
if(ket%4==0 and ket%100!=0 or ket%400==0):
    print("yes")
else:
    print("no")
