import random
l=[random.randint(1,100) for i in range(20)]
print("(a) The generated list :",l)
print("(b) The average of the elements in the list :",sum(l)/len(l))
print("(c) The largest element is %d and the smallest element is %d."%(max(l),min(l)))
l.sort()
print("(d) The second largest element is %d and the second smallest element is %d."%(l[-2],l[1]))
c=0
for i in l:
    if i%2==0:
        c+=1
print("(e) There are",c,"even numbers in the list.")