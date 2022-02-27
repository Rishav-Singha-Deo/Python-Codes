'''
3. Start with the list [7,9,11]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 7, 5, and 9 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
(g) Show the final list.
'''
l=[7,9,11]
l[1]=17#a
l.extend([7,5,9])#b
l.pop(0)#c
l.sort()#d
l=l*2#e
l.insert(3,25)#f
print("The final list :",l)#g