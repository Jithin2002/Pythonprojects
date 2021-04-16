import re
f2=open("validreg",'a') #either a append or w write
rule="([L][U][M]\d{2}[P][Y]\d{3}$)"
f=open("lumregno","r")
for num in f:
    number=num.rstrip("\n")
    matcher = re.fullmatch(rule,number)
    if matcher!= None:
        f2.write(number)
        f2.write("\n")
