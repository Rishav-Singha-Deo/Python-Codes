'''
Develop a Python Script that prompts the user to enter a list of
strings and then to create a new list that consists of those strings
with their first characters removed.
'''
print("Enter a list of strings, enter nothing to stop entering")
l,l1=[],[]
while 1:
    t=input("Enter the element : ")
    if t=="":
        break
    else:
        l.append(t)
for i in l:
    l1.append(i[1:])
print("The new list is :",l1)