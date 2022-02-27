'''
Write a function called merge that takes two already sorted lists of
possibly different lengths, and merges them into a single sorted list.
'''
def sorter(l):
    l1=[]
    for i in range(len(l)):
        l1.append(min(l))
        l.remove(min(l))
    return l1
def merge_sort(l1,l2):
    l=l1+l2
    return sorter(l)
l1,l2=[],[]
print("Enter the elements of the 1st list :-")
print("Enter 999 to stop")
while True:
    e=int(input("Enter the element : "))
    if e==999:
        break
    else:
        l1.append(e)
print("Enter the elements of the 2nd list :-")
print("Enter 999 to stop")
while True:
    e=int(input("Enter the element : "))
    if e==999:
        break
    else:
        l2.append(e)
print("The required list :",merge_sort(sorter(l1),sorter(l2)))