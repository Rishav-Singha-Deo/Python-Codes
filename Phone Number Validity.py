l=input("Enter a phone number : ").split("-")
s1,s2=["*","***","***","****"],["***","***","****"]
for i in range(len(l)):
    if l[i].isnumeric():
        l[i]="*"*len(l[i])
    else:
        print("Invalid")
        exit()
if l==s1 or l==s2:
    print("Valid")
else:
    print("Invalid")