import random
st1=input("Enter any message to encrypt : ")
st2,s="",[]
for i in range(len(st1)):
    if st1[i].isalpha():
        s.append(random.randint(1,26))
        if st1[i].isupper():
            c=chr(((ord(st1[i])-65+s[i])%26)+65)
            st2+=c
        if st1[i].islower():
            c=chr(((ord(st1[i])-97+s[i])%26)+97)
            st2+=c
    else:
        s.append(0)
        st2+=st1[i]
print("The key :",s)
print("The encrypted message :",st2)