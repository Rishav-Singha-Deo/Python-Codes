'''
Recall that if s is a string, then s.find(’a’) will find the location of
the first a in s. The problem is that it does not find the location of
every a. Write a function called find all that given a string and a
single character, returns a list containing all of the locations of that
character in the string. It should return an empty list if there are
no occurrences of the character in the string.
'''
def find(s,a):
    l=[]
    for i in range(len(s)):
        if s[i]==a:
            l.append(i)
    return l
s=input("Enter a string : ")
a=input("Enter the character to find : ")
print("The character",a,"appears at :",find(s,a))