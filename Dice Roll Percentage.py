import random
s=[random.randint(1,6)+random.randint(1,6) for i in range(10000)]
p=[(s.count(i)*100/10000) for i in range(2,13)]
print("The rolled number along with their chances :")
for i in range(11):
    print(i+2,": {}%".format(p[i]))