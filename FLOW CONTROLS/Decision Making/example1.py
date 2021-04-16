sal=int(input("enter your salary"))
year=int(input("enter your year of service"))
if(year>5):
    amount=(.05*sal)
    print("net bonus amount",amount)
else:
    print("no bonus",sal)

