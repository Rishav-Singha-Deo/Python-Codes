u=int(input("Enter the upper limit : "))
l=int(input("Enter the lower limit : "))
a=[]
for n in range(l,u+1):
    s=n**2
    l=len(str(s))
    p3,p4=0,0
    if l%2==0:
        p1=s//(10**(l//2))
        p2=s%(10**(l//2))
    else:
        p1=s//10**((l//2)+1)
        p2=s%10**((l//2)+1)
        p3=s//10**(l//2)
        p4=s%10**(l//2)
    if p1+p2==n or p3+p4==n:
        a.append(n)
print("All the Kaprekar Numbers within the range :",)
print(*a,sep=", ")