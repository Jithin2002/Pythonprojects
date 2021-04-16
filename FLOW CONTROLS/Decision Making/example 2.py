total=int(input("number of classes held"))
num=int(input("number of classes attended"))
per=(num/total)*100
if(per>75):
    print("percentage of class attented",per)
    print("allowed to sit in exam")
else:
    print("percentage of class attented",per)
    print("not allowed")