def base20(n):
    if n==0:
        return "0"
    b=""
    while n>0:
        d=int(n%20)
        if d<10:
            b+=str(d)
        else:
            b+=chr(ord('A')+d-10)
        n//=20
    b=b[::-1]
    return b
n=int(input("Enter a number in base 10 : "))
print("The number in base 20 :",base20(n))