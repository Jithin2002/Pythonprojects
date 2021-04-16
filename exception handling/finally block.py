lst=[18,4]
a=int(input("enter index"))
try:
    print(lst[a])
except:
    print("exception")
finally:
    print("inside finally")

finally block works at all time while either one of try or except block work at one time