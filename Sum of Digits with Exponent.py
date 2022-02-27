def sod2(n,l):
    if n<10:
        return n**l
    else:
        return ((n%10)**l)+sod2(n//10,l)
n=int(input("Enter any number : "))
print("Sum of digits :",sod2(n,len(str(n))))