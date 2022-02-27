'''
For this problem, use the dictionary whose keys are month names
and whose values are the number of days in the corresponding months.
• Ask the user to enter a month name and use the dictionary to
  tell them how many days are in the month.
• Print out all the keys in alphabetical order.
• Print out all the months with 31 days.
• Print out the (key-value) pairs sorted by the number of days in
  each month
• Modify the program from part (a) and the dictionary so that
  the user does not have to know how to spell the month name
  exactly. That is, all they have to do is spell the first three
  letters of the month name correctly.
'''
d={'January':31,'February':28,'March':31,'April':30,'May':31,
   'June':30,'July':31,'August':31,'September':30,'October':31,
   'November':30,'December':31}
m=input("Enter a month name : ")
if m in d:
    print("There are",d[m],"days in the month of",m)
else:
    print("Invalid month")
print("==========================================")
print("The keys in alphabetical order :-")
for i in sorted(d.keys()):
    print(i)
print("==========================================")
print("All the months with 31 days :-")
for i in d:
    if d[i]==31:
        print(i)
print("==========================================")
l31,l30,l28=[],[],["February : 28"]
for i in d:
    if d[i]==31:
        l31.append(i+" : "+str(d[i]))
    if d[i]==30:
        l30.append(i+" : "+str(d[i]))
print("Months with 30 days :-")
for i in l30:
    print(i)
print("==========================================")
print("Months with 31 days :-")
for i in l31:
    print(i)
print("==========================================")
print("Months with 28 days :-")
for i in l28:
    print(i)
print("==========================================")
m=input("Enter a month name : ")
ms=d.keys()
for i in ms:
    if m in i:
        m=i
if m in d:
    print("There are",d[m],"days in the month of",m)
else:
    print("Invalid month")
print("==========================================")