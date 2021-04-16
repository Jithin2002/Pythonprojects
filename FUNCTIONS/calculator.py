def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("select operations\n"
      "1. Add\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division")
select=int(input("select operations"))
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

if select==1:
    print(num1,"+",num2,"=",add(num1,num2))
