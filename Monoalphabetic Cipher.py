sl=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cl=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s=input("Enter the string to be ciphered : ")
k,sk,ck=[],[],[]
for i in range(26):
    print("Enter the key for",sl[i],":",end=" ")
    t=input()
    sk.append(t)
    ck.append(t.upper())
print("The ciphered string is :",end=" ")
for i in s:
    for j in range(26):
        if i == sl[j]:
            print(sk[sl.index(i)], end="")
        elif i == cl[j]:
            print(ck[cl.index(i)], end="")