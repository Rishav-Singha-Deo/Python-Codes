s=input("Enter any string : ")
v=["a","e","i","o","u"]
c=0
for i in s:
    if i in v:
        c=1
        break
if c==1:
    print("The string contains vowels")
else:
    print("The string doesn't contain any vowels.")