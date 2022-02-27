def firsr_diff(s1,s2):
    if s1==s2:
        return -1
    l=len(s2 if len(s1)>len(s2) else s1)
    if s1[:l]==s2[:l]:
        return l
    for i in range(l):
        if s1[i]!=s2[i]:
            return i
s1=input("Enter the first string : ")
s2=input("Enter the second string : ")
print("The first location of difference :",firsr_diff(s1,s2))