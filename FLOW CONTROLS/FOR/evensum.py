low=int(input("enter number"))
upp=int(input("enter number"))
evensum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("odd",oddsum)
print("even",evensum)