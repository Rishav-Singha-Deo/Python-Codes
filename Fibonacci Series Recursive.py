def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the no. of terms : "))
print("The result is :",fib(n-1))