f=open("numbers","r")
lst=[]


#to remove \n use function rstrip
for num in f:
        lst.append(int(num.rstrip("\n")))

print(lst)
print(sum(lst))
# lstrip
