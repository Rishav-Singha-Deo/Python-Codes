s=input("Enter any formula : ")
s=s.split("=")
o1,o2,c1,c2=0,0,0,0
for i in s[0]:
    if i=="(":
        o1+=1
    if i==")":
        c1+=1
for i in s[1]:
    if i=="(":
        o2+=1
    if i==")":
        c2+=1
if o1>c1:
    print("You have unclosed parentheses in LHS.")
if o2>c2:
    print("You have unclosed parentheses in RHS.")
if o1<c1:
    print("You have unopened parentheses in LHS.")
if o2<c2:
    print("You have unopened parentheses in RHS.")
if o1==c1 and o2==c2:
    print("The parentheses are okay.")