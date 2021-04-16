import re
f2=open("validphonereg",'a')
x = '[+][9][1]\d{10}'
f=open("numbervalid","r")
for num in f:
    number=num.rstrip("\n")
    matcher = re.fullmatch(x,number)
    if matcher!= None:
        f2.write(number)
        f2.write("\n")

