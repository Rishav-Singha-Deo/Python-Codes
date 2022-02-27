print("Enter a list of integers, enter 999 to stop entering")
l,i=[],0
while i>-1:
    print("No.",i+1,":",end=" ")
    t=int(input())
    if t==999:
        break
    else:
        l.append(t)
        i+=1
print("(a) Total number of items in the list :",len(l))
print("(b) The last item in the list :",l[-1:])
print("(c) The list in reverse :",l[::-1])
print("(d) Yes the list contains '5'.") if 5 in l else print("(d) No the list doesn't contain '5'.")
print("(e) There are",l.count(5),"'5' in the list.")
l.pop(0);l.pop(-1);l.sort()
print("(f) The updated list :",l)
c=0
for i in l:
    if i<5:
        c+=1
print("(g) There are",c,"items less than '5'.")