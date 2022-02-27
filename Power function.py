def pow(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*pow(a,b-1)
a=int(input("Enter the number : "))
b=int(input("Enter the power : "))
print("The result is :",pow(a,b))