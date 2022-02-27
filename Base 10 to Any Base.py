def to_any_base(n,b):
    bn=""
    while n>0:
        d=int(n%b)
        if d<10:
            bn+=str(d)
        else:
            bn+=chr(ord('A')+d-10)
        n//=b
    bn=bn[::-1]
    return bn
n=int(input("Enter a number in base 10 : "))
b=int(input("Enter the base to convert to : "))
print("The number in base",b,":",to_any_base(n,b))