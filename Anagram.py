import random
s,s1=list(input("Enter a string : ")),[]
for i in range(len(s)):
    c=random.choice(s)
    s1.append(c)
    s.remove(c)
print("The random anagram :","".join(s1).capitalize())