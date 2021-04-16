lst=[1,5,4,7,8,6,9]
lst.sort()
print(lst)
element=int(input("enter number"))
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2

    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")