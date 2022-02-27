def squarefree(n):
    l=[]
    for i in range(2,int(n/2)+1):
        if n%i==0:
            l.append(i)
    l.append(n)
    for i in range(len(l)):
        if l[i]==int(l[i]**(1/2))**2:
            return False
    return True
n=int(input("Enter a number : "))
if squarefree(n):
    print("It is squarefree.")
else:
    print("It is not squarefree.")