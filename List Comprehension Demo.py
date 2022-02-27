'''
Let L be a list of strings. Write list comprehensions that create new lists from L for each of the following:
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
'''
l="Upcoming IEEE International Conference ICCECE 2020 will be held on the 17th & 18th of January 2020".split(" ")
l1=[s[1:] for s in l]
l2=[len(s) for s in l]
l3=[s for s in l if len(s)>=3]
print("(a)",l1)
print("(b)",l2)
print("(c)",l3)