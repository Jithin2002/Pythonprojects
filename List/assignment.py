# lst=[3,4,8]   3+4+8=15
# output  lst1=[12,11,7]   15-3=12
#
# lst=[5,10,20]  5+10+20=35
# output  lst1=[10,25,15]   35-5=30

lst=[3,4,8]
lst1=[]
lstsum=sum(lst)
print(lstsum)
for i in lst:
    j=lstsum-i
    lst1.append(j)
print(lst1)
