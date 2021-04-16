# index error
a=[1,2,3]
try:
    i=int(input("index"))
    print(a[i])
except Exception as e:
    print("excption eoccured")