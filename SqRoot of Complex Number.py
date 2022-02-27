def sqroot(a,b):
    i=-1
    z=((a+(i*b))**2)**0.5
    return (((z+a)/2)**0.5)+((i*b/(b**2)**0.5)*(((z-a)/2)**0.5))
print("In the complex number a+ib")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print("The square root is :",sqroot(a,b))