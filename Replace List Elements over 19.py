'''
Develop a Python script that prompts the user to enter a list containing
numbers between 11 and 22. Then replace all of the entries
in the list that are greater than 19 with 19.
'''
print("Enter a list of integers(between 11 & 22), enter 999 to stop entering")
l,i=[],0
while 1:
    t=int(input("Enter the element : "))
    if t==999:
        break
    if t<11 or t>22:
        print("Invalid Input")
    else:
        l.append(t)
for i in range(len(l)):
    if l[i]>19:
        l[i]=19
print("The new list is :",l)