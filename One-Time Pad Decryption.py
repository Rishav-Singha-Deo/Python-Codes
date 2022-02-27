st1=input("Enter the message to decrypt : ")
print("Enter the key")
s=[]
for i in range(len(st1)):
    print("Key no.",i+1,":",end=" ")
    s.append(int(input())*(-1))
st2=""
for i in range(len(st1)):
    if st1[i].isalpha():
        if st1[i].isupper():
            c=chr(((ord(st1[i])-65+s[i])%26)+65)
            st2+=c
        if st1[i].islower():
            c=chr(((ord(st1[i])-97+s[i])%26)+97)
            st2+=c
    else:
        st2+=st1[i]
print("The decrypted message :",st2)