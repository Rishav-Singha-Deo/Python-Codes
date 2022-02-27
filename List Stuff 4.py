'''
Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column.
'''
import random
l=[[random.randint(1,100) for i in range(10)] for j in range(10)]
print("(a) The list :")
for i in l:
    print(i)
print("\n(b) The largest value in the third row :",max(l[2]))
print("\n(c) The smallest value in the 6th column :",min([l[i][5] for i in range(len(l))]))