import re
n=input("enter mail")
rule="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")