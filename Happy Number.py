u=int(input("Enter the upper limit : "))
l=int(input("Enter the lower limit : "))
a=[]
def sod(n):
    s=0
    while (n>0):
        s+=((n%10)**2)
        n//=10
    return s
for n in range(l,u+1):
    tmp=n
    while (tmp!=1 and tmp!=4 and tmp!=7):
        tmp=sod(tmp)
    if tmp==1 or tmp==7:
        a.append(n)
print("All the Happy Numbers within this range :",end=" ")
print(*a,sep=", ")