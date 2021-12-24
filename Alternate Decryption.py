s=input("Enter a string to be decrypted : ")
if len(s)%2!=0:
    s+=" "
f,l=s[0:len(s)//2],s[-len(s)//2:]
n=""
for i in range(len(s)//2):
    n+=f[i]+l[i]
print("The decrypted string is : ",n)