def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def binom(n,k):
    return (fact(n)/(fact(k)*fact(n-k)))
n=int(input("Enter the value of n : "))
k=int(input("Enter the value of k : "))
print("The binomial coefficient is :",binom(n,k))