def cubeofnum():
    num=int(input("enter number"))
    cube=1
    for i in range(1,4):
        cube*=num
    print(cube)
cubeofnum()