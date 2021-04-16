#lambda functions
#
#map()
#filter()
#reduce()

# lst=[20,30,40,50]
# squ=[]
# for num in lst:
#     res=num**2
#     squ.append(res)
# print(squ)


# def squ(no):
#     return no**2
# squares=list(map(squ,lst))
# print(squares)
#
# squares=list(map(lambda no:no**2,lst))
# print(squares)

lst=[2,3.,4,5,6,7]
cube=list(map(lambda no : no**3,lst))
print(cube)