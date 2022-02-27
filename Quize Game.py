import random
q=["What is the square root of 144?","What is the cube of 8?",
   "There is a finite amount of numbers. True or False?",
   "How many planets are there in our solar system?",
   "Dinosaurs are all alive. True or False?",
   "LCM of 12, 15, and 75?","HCF of 8, 12, and 20?",
   "The earth's ______ pulls every thing towards it.",
   "The earth's gravity is ______ m/s^2.",
   "How many letters are there in the English Alphabet?"]
a=["12","512","False","8","False","300","4","gravity","9.8","26"]
o=[["10","12","11","13"],["500","640","512","240"],["True","False"],
   ["7","8","9","10"],["True","False"],["100","200","300","400"],
   ["3","4","5","6"],["gravity","humidity","atmosphere","water bodies"],
   ["1.7","10.5","9.8","8.9"],["24","25","26","27"]]
c=0
for i in range(4):
   s=random.choice(q)
   random.shuffle(o[q.index(s)])
   print("===================================================")
   print(s)
   for j in range(len(o[q.index(s)])):
      print(j+1,":",o[q.index(s)][j])
   ch=int(input("Enter your choice : "))
   if a[q.index(s)]==o[q.index(s)][ch-1]:
      c+=1
   o.remove(o[q.index(s)])
   a.pop(q.index(s))
   q.remove(s)
print("===================================================")
print("You scored",c,"out of 4.")