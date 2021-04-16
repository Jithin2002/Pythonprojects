# operation in set
#  union
#  intersection
#  difference

set1={1,2,3,4,5,6}
set2={5,5,6,7,8,9,10}

#union 1,2,3,4,5,6,7,8,9,10

set3=set1.union(set2)
print(set3)

#interrsection 5,6
set4=set1.intersection(set2)
print(set4)

#difference 1,2,3,4
set5=set1.difference(set2)
print(set5)

difference function
# return a new set with all items fro both sets by removing duplicates
# return a set of all elemenromn either a or b but not in both
# remove item from set1 that are not common to both set1 and set2