def per(s,n):
    if (len(s)==0):
        print(n,end=" ")
        return
    for i in range(len(s)):
        c,l,r=s[i],s[0:i],s[i+1:]
        t=l+r
        per(t,n+c)
s=input("Enter a word : ")
print("All possible permutations are : ")
per(s,"")