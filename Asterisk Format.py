s=input("Enter an algebraic expression : ")
s+=" "
for i in range(len(s)*2):
    if s[i]==" ":
        break
    if s[i] in "1234567890":
        if s[i+1].isalpha()==True:
            s=s[0:i+1]+"*"+s[i+1:]
    if s[i]=="(":
        if s[i-1].isalpha()==True or s[i-1] in "1234567890":
            s=s[0:i]+"*"+s[i:]
    if s[i]==")":
        if s[i+1].isalpha()==True or s[i+1] in "1234567890":
            s=s[0:i+1]+"*"+s[i+1:]
print("The expression with asterisk inserted :",s)