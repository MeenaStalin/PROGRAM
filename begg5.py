n123,n234,n345=input().split(" ")
if(n123>n234):
    if(n123>n345):
        print(n123)
    else:
        print(n345)
elif(n234>n345):
    print(n234)
else:
    print(n345)
