u=int(input("Enter the upper limit : "))
l=int(input("Enter the lower limit : "))
a=[]
def hyp(n):
    p=1
    for i in range(1,n+1):
        p*=pow(i,i)
    return p
for i in range(l,u+1):
    if hyp(i)<=u:
        a.append(hyp(i))
print("All the Hyperfactorial Numbers within this range :",end=" ")
print(*a,sep=", ")