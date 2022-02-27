'''
Write a function called closest that takes a list of numbers L and
a number n and returns the largest element in L that is not larger
than n. For instance, if L=[1,6,3,9,11] and n=8, then the function
should return 6, because 6 is the closest thing in L to 8b that is
not larger than 8. Don’t worry about if all of the things in L are
smaller than n.
'''
import random
def closest(l,n):
    c=0
    for i in l:
        if i<n and i>c and i<n:
            c=i
    return c
l,n=[random.randint(0,10) for i in range(random.randint(5,10))],random.randint(1,10)
print("The list :",end=" ")
for i in l:
    print(i,end=" ")
print("\nThe value of n :",n)
print("The required element is :",closest(l,n))