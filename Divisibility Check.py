def div(n1,n2):
    if n1%n2==0:
        return 1
    else:
        return 0
n1=int(input("Enter the dividend : "))
n2=int(input("Enter the divisor : "))
if div(n1,n2)==1:
    print("Yes,",n1,"is divisible by",n2,end=".")
else:
    print("No,",n1,"is not divisible by",n2,end=".")