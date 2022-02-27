def calc(a,b,o):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*" or o=="x" or o=="X":
        return a*b
    elif o=="/":
        return a/b
    elif o=="//":
        return a//b
    elif o=="%":
        return a%b
    elif o=="**" or o=="^":
        return a**b
    else:
        print("No such operator here.")
a=int(input("Enter the first numbers : "))
b=int(input("Enter the second numbers : "))
o=input("Enter an operator operator : ")
print("The result :",calc(a,b,o))