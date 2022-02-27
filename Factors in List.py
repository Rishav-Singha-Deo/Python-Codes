'''
Write a program that asks the user for an integer and creates a list
that consists of the factors of that integer.
'''
n,l=int(input("Enter any integer : ")),[]
for i in range(1,int(n/2)+1):
    if n%i==0:
        l.append(i)
l.append(n)
print("The list with the factors :",l)