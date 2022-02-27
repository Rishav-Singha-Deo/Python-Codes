def sod(n):
    if n<10:
        return n
    else:
        return (n%10)+sod(n//10)
n=int(input("Enter any number : "))
print("Sum of digits :",sod(n))