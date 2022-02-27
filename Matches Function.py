'''
Write a function called matches that takes two strings as arguments
and returns how many matches there are between the strings. A
match is where the two strings have the same character at the same
index. For instance, ’python’ and ’path’ match in the first, third,
and fourth characters, so the function should return 3.
'''
def matches(s1,s2):
    c=0
    if len(s1)>len(s2):
        m=s2
    else:
        m=s1
    for i in range(len(m)):
        if s1[i]==s2[i]:
            c+=1
    return c
s1=input("Enter the 1st string : ")
s2=input("Enter the 2nd string : ")
print("There are",matches(s1,s2),"match(es).")