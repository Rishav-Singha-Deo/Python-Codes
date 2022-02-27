def arm(n,l):
    if len(str(n))==1:
        return n**l
    else:
        return ((n%10)**l)+arm(n//10,l)
n=int(input("Enter a number : "))
if arm(n,len(str(n)))==n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")