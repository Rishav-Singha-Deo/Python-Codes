s=input("Enter the string to be ciphered : ")
print("The converted cipher text is : ",end="")
for i in s:
    if i==' ':
        print(" ",end="")
    c=ord(i)
    if (c>=33 and c<=64) or (c>=91 and c<=96) or c>=123:
        i=chr(c)
        print(i,end="")
    if c>=65 and c<=90:
        c=((c-65+(-3))%26)+65
        i=chr(c)
        print(i,end="")
    elif c>=97 and c<=122:
        c=((c-97+(-3))%26)+97
        i=chr(c)
        print(i,end="")