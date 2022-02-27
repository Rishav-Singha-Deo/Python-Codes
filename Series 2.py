def series2(n):
    if n==2:
        return 2
    else:
        return n+series2(n-2)
n=int(input("Enter the no. of terms : "))
print("The sum is :",series2(n*2))