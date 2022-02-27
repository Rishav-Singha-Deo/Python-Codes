def nod(n):
    if n<10:
        return 1
    else:
        return 1+nod(n//10)
n=int(input("Enter any number : "))
print("No. of digits :",nod(n))