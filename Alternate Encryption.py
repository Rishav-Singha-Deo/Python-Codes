s=input("Enter a string to be encrypted : ")
o,e="",""
if len(s)%2!=0:
    s+=" "
for i in range(0,len(s),2):
    o+=s[i]
    e+=s[i+1]
print("The encrypted string is : %s%s"%(o,e))