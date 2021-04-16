# zero division error
# a=int(input("no1"))
# b=int(input("no2"))
# c=a/b
# print(c)

no1=int(input("enter no1"))
no2=int(input("enter no2"))
try:
    res=no1/no2
    print("res=", res)
except:
    print("exception occured")

#only one block work at a time
