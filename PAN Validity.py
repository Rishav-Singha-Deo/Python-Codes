s=input("Enter your PAN : ")
if len(s)==10:
    if s[:5].isalpha() and s[-1:].isalpha():
        if s[5:9].isnumeric():
            print("Valid PAN card")
        else:
            print("Invalid PAN card")
else:
    print("Invalid PAN card")