#print employee name whose salary greater than 17000
employee=[[1001,"arjun",15000],
          [1002,"arun",20000],
          [1003,"vinu",25000],
          [1004,"binu",10000]]
for i in employee:
    if(i[2]>17000):
        print(i[1])
    