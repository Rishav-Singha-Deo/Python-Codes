s=input("Enter the string to be converted : ")
k=int(input("Enter the key : "))
print("The converted cipher text is : ",end="")
for i in s:
    if i==' ':
        print(" ",end="")
    c=ord(i)
    if c>=65 and c<=90:
        c=((c-65+k)%26)+65
        i=chr(c)
        print(i,end="")
    elif c>=97 and c<=122:
        c=((c-97+k)%26)+97
        i=chr(c)
        print(i,end="")