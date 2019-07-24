m1=int(input(''))
k2=[]
for i in range(0,m1):
    k2.append(input())
m2=len(k2[0])
k3=""
for i in range(0,m1):
    k4=k2[0][i]
    k5=0
    for j in range(0,m1):
        if(k4!=k2[j][i]):
            k5=1
    if(k5==0):
        k3=k3+k4
    else:
        break
print(k3)
