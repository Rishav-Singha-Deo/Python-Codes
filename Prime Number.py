def isprime(n):
    c=0
    if n>1:
        for i in range(2,int(n**(1/2))+1):
            if n%i==0:
                c=1
                break
        if c==0:
            return 1
        else:
            return 0
n=eval(input("Enter any number : "))
if isprime(n):
    print("Prime Number")
else:
    print("Not Prime Number")