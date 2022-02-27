def primes(n,j):
    l=[]
    while n>0:
        c=0
        for i in range(2,int(j**(1/2))+1):
            if j%i==0:
                c=1
                break
        if c==0:
            l.append(j)
            n-=1
        j+=1
    return l
j,n=2,100
print(primes(n,j))