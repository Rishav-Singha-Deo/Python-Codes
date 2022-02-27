def binary_search(l,lw,hg,x):
    if hg>=lw:
        m=(hg+lw)//2
        if l[m]==x:
            return m
        elif l[m]>x:
            return binary_search(l,lw,m-1,x)
        else:
            return binary_search(l,m+1,hg,x)
    else:
        return -1
WORDS=["a","b","c","d","e","f","g","h","i","j",
       "k","l","m","n","o","p","q","r","s","t",
       "u","v","w","x","y","z","A","B","C","D",
       "E","F","G","H","I","J","K","L","M","N",
       "O","P","Q","R","S","T","U","V","W","X",
       "Y","Z"]
x="w"
ser=binary_search(WORDS,0,len(WORDS)-1,x)
if ser!=-1:
    print("Element is present at index :",ser)
else:
    print("Element is not present in the list.")