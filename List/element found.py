lst=[2,3,4,5,6,7,8]
num=int(input("enter a number"))
flag=0
for i in lst:
    if(i==num):
        flag=1
        break
    else:
        flag=0
if(flag>0):
    print("element found")
else:
    print("not found")
#this program is caled linear search
# we have to search everytime wheather element is thereor not
# drawback increases complexity
# to overcome this we use binary search

