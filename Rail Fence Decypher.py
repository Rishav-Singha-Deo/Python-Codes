s=input("Enter a string to be decrypted : ")
k=int(input("Enter the key : "))
e=[["" for i in range(len(s))] for j in range(k)]
f,r,l,c=0,0,0,[]
for i in range(len(s)):
    e[r][i]="-"
    if r==0:
        f=1
    elif r==k-1:
        f=0
    if f==1:
        r+=1
    else:
        r-=1
for i in range(k):
    for j in range(len(s)):
        if e[i][j]=="-" and l<len(s):
            e[i][j]=s[l]
            l+=1
for i in range(len(s)):
    if r==0:
        f=1
    if r==k-1:
        f=0
    if e[r][i]!="-":
        c.append(e[r][i])
    if f==1:
        r+=1
    else:
        r-=1
print("The decrypted string is :","".join(c))