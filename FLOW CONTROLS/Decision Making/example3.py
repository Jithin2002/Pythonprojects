age=int(input("enter your age"))
sex=input("enter your sex")
maritial=input("enter your maritial status")
if(sex=='f'):
    print("she wil work only in urban areas")
elif(sex=='m'):
    if(20<age<40):
        print("he may work in anywhere")
    elif(age>41):
        print("he will work in urban areas")
    else:
        print("error")
