def isprime(n):
    c=0
    if n>1:
        for i in range(2,int(n**(1/2))+1):
            if n%i==0:
                c=1
                break
            else:
                return 1
        if c==0:
            return 1
        else:
            return 0
p,c=[],[]
u=int(input("Enter the upper limit : "))
l=int(input("Enter the lower limit : "))
for i in range(l,u+1):
    if i==1:
        continue
    elif isprime(i):
        p.append(i)
    else:
        c.append(i)
print("The Primes in the range :",p)
print("The composites in the range :",c)