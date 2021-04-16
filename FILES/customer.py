f=open("/Users/USER/Downloads/customer")
for lines in f:
    data=lines.rstrip("\n").split(",")
    fname=data[1]
    age=data[3]
    loc=data[-1]
    print(data)
    print(fname,",",age,",",loc)