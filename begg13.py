cone=int(input())
if(cone>1):
    for i in range(2,cone):
        if(cone%i==0):
            print("no")
            break
    else:
        print("yes")
