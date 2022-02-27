s,t=input("Enter a string : "),""
for i in s:
    if i in "aeiouAEIOU":
        continue
    t+=i
print("The string with the vowels removed is :",t)