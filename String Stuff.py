s=input("Enter any string : ")
print("(a) Total number of characters :",len(s))
print("(b) The string repeated 5 times :")
for i in range(1,(5+1)):
    print("%d. %s"%(i,s))
print("(c) The first character of the string :",s[0])
print("(d) The first four characters of the string :",s[0:4])
print("(e) The last two characters of the string :",s[-2:])
print("(f) The string in reversed form :",s[::-1])
if len(s)>=9:
    print("(g) The ninth character of the string :", s[9-1])
else:
    print("(g) The string is too short for a ninth character.")
print("(h) The string with its first and last characters removed :",s[1:-1])
print("(i) The string in all the letters in capital form :",s.upper())
st1=""
for i in s:
    if i=="i":
        st1+="I"
    else:
        st1+=i
print("(j) The string with every 'i' replaced with an 'I' :",st1)
st2=""
for i in s:
    c=ord(i)
    if (c>=65 and c<=90) or (c>=97 and c<=122):
        st2+=" "
    else:
        st2+=i
print("(k v1) The string with every letter replaced by a space :",st2)
st3=""
for i in s:
    st3+=" "+i
print("(k v2) The string with every letter replaced by a space :",st3)