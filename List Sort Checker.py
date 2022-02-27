'''
Write a function called is_sorted that is given a list and returns
True if the list is sorted and False otherwise.
'''
def is_sorted(l):
    if sorted(l)==l:
        return True
    else:
        return False
print("Enter the elements to this list")
print("Enter 999 to stop")
l=[]
while True:
    e=int(input("Enter an element : "))
    if e==999:
        break
    else:
        l.append(e)
if is_sorted(l)==True:
    print("It is sorted.")
else:
    print("It isn't sorted.")