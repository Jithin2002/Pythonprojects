lst=[]
lst2=[]
lst3=[]
for i in range(50,201):
     lst.append(i)
print(lst)
for i in range(50,201):
    if(i%2==0):
        lst2.append(i)
    else:
        lst3.append(i)
print("evenlist=",lst2)
print("oddlist=",lst3)