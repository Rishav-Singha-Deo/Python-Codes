def ispalin(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return ispalin(s[1:-1])
        else:
            return False
s=input("Enter a string : ")
if ispalin(s)==True:
    print("Palindrome.")
else:
    print("Not a Palindrome.")