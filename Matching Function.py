'''
Develop a function named Matching that takes two strings and
returns True if the strings are of the same length but differ in exactly
one letter, like like/mike or Dear/Deer.
'''
def matching(s1,s2):
    if len(s1)==len(s2):
        c=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
        if c==1:
            return True
        else:
            return False
    else:
        return False
s1=input("Enter the 1st string : ")
s2=input("Enter the 2nd string : ")
if matching(s1,s2):
    print("Fulfills the condition")
else:
    print("Doesn't fulfills the condition")