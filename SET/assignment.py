lst=[1,2,3,4,5,6]

# read an element from list6
# return pairs (2,4)

num=int(input("an elemnt from list"))
for i in lst:
    for j in lst:
        sum=0
        sum=i+j
        if(sum==num):
            print("(",i,j,")")

