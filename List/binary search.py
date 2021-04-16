#algorithm

# 1. Sorting
# lst=[7,4,1,2,3]
lst.sort()
# after sorting
# lst=[1,2,3,4,7]
#
# 2.set lower and upper
# low=0
# upp=len(lst)-1
#
# 3.calculate mid
#  mid=(low+upp)//2
#  (0+4)//2= 2 lst[2]

# 3.conditions
#
# if(element>lst(mid))
#     if condition is true
#         low=mid+1
#
# if(element,lst(mid))
#     upp=mid-1
#
# if(element==lst(mid))
#     return element found
#