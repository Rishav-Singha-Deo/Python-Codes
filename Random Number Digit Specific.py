from random import randint
def spdirand(n):
    u=10**(n-1)
    l=(10**n)-1
    return randint(u,l)
n=int(input("Enter the number of digits : "))
print("he random number :",spdirand(n))