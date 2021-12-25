s=input("Enter any string : ")
print("(a) Total number of characters :",len(s))
print("(b) The string repeated 5 times :\n",s*5)
print("(c) The first character of the string :",s[0])
print("(d) The first four characters of the string :",s[0:4])
print("(e) The last two characters of the string :",s[-2:])
print("(f) The string in reversed form :",s[::-1])
print("(g) The ninth character of the string :", s[9-1] if len(s)>=9
else "(g) The string is too short for a ninth character.")
print("(h) The string with its first and last characters removed :",s[1:-1])
print("(i) The string in all the letters in capital form :",s.upper())
print("(j) The string with every 'i' replaced with an 'I' :",s.replace("i","I"))
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
