import random
n=[]
a=int(input("How many names will you enter : "))
print("Start entering :\n=================")
for i in range(a):
   n.append(input("Enter a name : "))
   f=int(input("Enter the frequency of the name : "))
   for j in range(f-1):
      n.append(n[-1])
   print("===================================")
print("The name out of the hat is :",random.choice(n))