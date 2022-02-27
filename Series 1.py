def series(x,n):
    if n==1:
        return x
    else:
        return ((x**n)/n)+series(x,n-1)
x=int(input("Enter the value of x : "))
n=int(input("Enter the no. of terms : "))
print("The sum is :",series(x,n))