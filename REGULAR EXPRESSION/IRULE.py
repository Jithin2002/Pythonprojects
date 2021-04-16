import re
# n= "helloo"
# x= '\w{6}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
#
# n = "56kg"
# x = '\d{2}[a-z]{2}'
# match = re.fullmatch(x, n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
#
# n = input("enter the number to validate")
# x = '\d{10}'
# match = re.fullmatch(x, n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re

n = input("enter the number to validate")
x = '[+][9][1]\d{10}'
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")