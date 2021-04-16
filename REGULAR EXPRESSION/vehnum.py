import re
valid=[]
rule="[Kk][Ll]\d{2}[a-zA-Z]{2}\d{4}$"
f=open("vehnum","r")
for num in f:
    number=num.rstrip("\n")
    matcher = re.fullmatch(rule,number)
    if matcher!= None:
        valid.append(number)
        print(number)
print("valid")
