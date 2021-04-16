# import re
# x="[abc]" #either a,b or c
# matcher = re.finditer(x, "abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#

# import re
#
# x = "[a-z]"
# matcher = re.finditer(x, "abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x = "\s"
# matcher = re.finditer(x, "abt c@5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# QUANTIFIERS


# import re
#
# x = "a+"
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = "a*" #count including zero number of a
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x = "a?" #count a as each including zero number of a
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = "a{3}" #no of position
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x = "a{1,3}" #minimum 2 a and maximum 3 a
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = "^a" #check starting with a
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = "a$" #check ending with a
# r= "aaa abc aaaaa cga"
# matcher = re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())