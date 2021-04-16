low=int(input("enter a number"))
upp=int(input("enter a number"))
flag=0
for i in range(low,upp):
    for j in range(2,i):
        if(i%j==0):
            flag=0
            break
        else:
            flag=1
    if(flag>0):
        print(i)


