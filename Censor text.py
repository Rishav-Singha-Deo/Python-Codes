c=["darn","dang","freakin","heck","shoot"]
s=input("Enter a text : ").split(" ")
for i in range(len(s)):
    for j in c:
        if j in s[i].lower():
            s[i]=s[i].lower().replace(j,"*"*len(j))
print("The censored text :"," ".join(s))