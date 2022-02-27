import random
l=[random.randint(1,100) for i in range(10)]
print("The initial list :",l)
l=l[-1:]+l[:len(l)-1]
print("The rotated list :",l)