def cubeofnum(num):
    cube=1
    for i in range(1,4):
        cube*=num
    return cube
out=cubeofnum(6)
print(out)