# How to create an empty set
#  we have to use a set function
#
# if we use set={} it is a dictionary , if the curly bracket has values it is a set
set1={}
print(type(set1))

set={1,2,3,4,10.5,"sabir",True} #supports heterogenous data
#true doesnot print in this set because duplicate value doesnot support value of true is 1
print(type(set))
print(set)

set2={1,2,3,4,1,1}
print(set2)

set3={10,15,20,1,2,3,"sabir",0.5,0,5,100}
print(set3)  #insertion order not preserved

#set is mutable