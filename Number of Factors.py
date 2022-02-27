def number_of_factors(n):
    s=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s+=1
    return s
n=int(input("Enter a number : "))
print("The number has",number_of_factors(n),"factors")