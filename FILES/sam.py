f=open("data","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
print(words)