def isprime(n):
    if n==1:
        return 2
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 0
        else:
            return 1
def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)
p,q=11,17
n=p*q
phi=(p-1)*(q-1)
e=2
while e<phi:
    if gcd(e,phi)==1:
        break
    e+=1
k=0
for k in range(1,e):
    if (1+k*phi)%e==0:
        break
d=int((1+k*phi)/e)
print("Public key :",e,n)
print("Private key :",d,n)
print("k :",k)
m=45
c=(m**e)%n
print("The encrypted message :",c)
m=(c**d)%n
print("The decrypted message :",m)