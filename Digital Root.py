def droot(n):
    if len(str(n))==1:
        return n
    else:
        s=0
        for i in str(n):
            s+=int(i)
        return droot(s)
n=int(input("Enter a number : "))
print("The digital root is :",droot(n))