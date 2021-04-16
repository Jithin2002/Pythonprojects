#5!

#5*4*3*2*1

def factorial():
    num=int(input("enter number"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
factorial()