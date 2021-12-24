s=input("Enter a large number : ")
t=[]
for i in range(0,len(s),3):
    t.append(s[-3:])
    s=s[0:-3]
t.reverse()
print("The required string is :",",".join(t),end=".")