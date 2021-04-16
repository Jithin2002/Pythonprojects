evenlst=[]
oddlist=[]
f=open("numbers","r")
for num in f:
    data=int(num.rstrip("\n"))
    if(data%2==0):
        evenlst.append(int(num.rstrip("\n")))
    else:
        oddlist.append(int(num.rstrip("\n")))
print(evenlst)
print(oddlist)