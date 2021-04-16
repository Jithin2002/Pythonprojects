num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("number2",num2)
    else:
        print("number3",num3)
elif(num2>num3)&(num2>num1):
    if(num3>num1):
        print("number3",num3)
    else:
        print("number1",num1)
elif(num3>num2)&(num3>num1):
    if(num1>num2):
        print("number1",num1)
    else:
        print("number2",num2)
        