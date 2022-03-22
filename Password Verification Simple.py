pw=input("Enter the password : ")
a,b,c=ord(pw[0]),ord(pw[-1]),0
if len(pw)>=8:
    if a>=65 and a<=90 and b>=97 and b<=122:
        for i in pw:
            if i.isdigit():
                c+=1
        if c>0:
            print("Password verified")
        else:
            print("At least 1 digit needed")
    else:
        print("1st letter upper and last letter lower required")
else:
    print("At least 8 characters needed")