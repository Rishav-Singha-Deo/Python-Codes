s=input("Enter a string to be encrypted : ")
k=int(input("Enter the key : "))
e=[["" for i in range(len(s))] for j in range(k)]
f,r=0,0
for i in range(len(s)):
    e[r][i]=s[i]
    if r==0:
        f=0
    elif r==k-1:
        f=1
    if f==0:
        r+=1
    else:
        r-=1
c=[]
for i in range(k):
    for j in range(len(s)):
        c.append(e[i][j])
print("The encrypted string is :","".join(c))