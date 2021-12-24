'''
Develop a program for the following activities:
(a) Without using the in operator, the program asks the user for
a string and a letter and prints out whether or not the letter
appears in the string.
(b) Without using the count method, the program asks the user
for a string and a letter and counts how many times the letter
occurs in the string.
(c) Without using the index method, the program that asks the
user for a string and a letter and prints out the index of the
first occurrence of the letter in the string. If the letter is not in
the string, the program should say so.
'''
s=input("Enter a string : ").lower()
l=input("Enter a letter : ")
c=s.count(l)
if c>0:
    print("Yes, the string contains the letter.")
else:
    print("No, the string does not contain the letter.")
c=0
for i in s:
    if i==l:
        c+=1
print("The letter occurs",c,"times in the string.")
c,f=0,0
for i in s:
    if i==l:
        f=1
        break
    c+=1
if f==1:
    print("The first occurrence of the letter in the string is at index[%d]" % c)
else:
    print("There are no occurrences of the letter in the string.")