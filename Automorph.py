u=int(input("Enter the upper limit : "))
l=int(input("Enter the lower limit : "))
a,t,ta=[],[],[]
for n in range(l,u+1):
    if n==(n**2)%(10**(len(str(n)))):
        a.append(n)
    if n==(n**3)%(10**(len(str(n)))):
        t.append(n)
    if n==(3*(n**2))%(10**(len(str(n)))):
        ta.append(n)
print("Automorphic : ",end="")
print(*a,sep=", ")
print("Trimorphic : ",end="")
print(*t,sep=", ")
print("Tri-automorphic : ",end="")
print(*ta,sep=", ")