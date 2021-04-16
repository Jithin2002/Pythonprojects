def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
data=factorial(6)
print(data)