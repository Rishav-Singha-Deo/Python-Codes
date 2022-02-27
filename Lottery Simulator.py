import random
l1,c=[random.randint(1,10) for i in range(6)],0
for i in range(1000):
   l2=[random.randint(1,10) for j in range(6)]
   if l1==l2:
      c+=1
print("The average number of drawings needed over 1000 times :",(c/1000))