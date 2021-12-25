s=input("Enter any string : ")
c=0
for i in s:
    if i in "aeiouAEIOU":
        print("The string contains vowels")
        exit()
print("The string doesn't contain any vowels.")
