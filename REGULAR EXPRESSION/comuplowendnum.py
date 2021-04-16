import re
n=input("enter ")
rule="([a-zA-Z]+\d{1}$)"
match=re.fullmatch(rule,n)
if match is not None:
    print("valid")
else:
    print("invalid")