c=input("Enter the chosen letter : ")
s=input("Enter the word containing the letter : ")
t=1
if c in s:
    for i in s:
        if i==c:
            break
        t+=1
    s=s[0:t]+"\n"+s[t:]
    print("The required output is :\n%s"%s)
else:
    print("Your word doesn't contain the chosen letter.")