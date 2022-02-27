'''
We usually refer to the entries of a two-dimensional list by their row
and column, like below on the left. Another way is shown below on
the right. (0,0) (0,1) (0,2) 0 1 2 (1,0) (1,1) (1,2) 3 4 5 (2,0)
(2,1) (2,2) 6 7 8
• Write some code that translates from the left representation to
the right one. The // and % operators will be useful. Be sure
your code works for arrays of any size.
• Write some code that translates from the right representation
to the left one.
'''
n=int(input("Enter the no.of rows : "))
m=int(input("Enter the no.of columns : "))
l=[[(i,j) for j in range(m)] for i in range(n)]
print("\nThe left side way :")
for i in l:
    for j in i:
        print(j,end="")
    print()
print("\nThe translated way :")
for i in range(n):
    for j in range(m):
        t=l[i][j][0]+1
        print((t*m)-m+j,end="  ")
    print()
print()
n=int(input("Enter the no.of rows : "))
m=int(input("Enter the no.of columns : "))
l=[i for i in range(n*m)]
l2,c=[],0
for i in range(n):
    l1=[]
    for j in range(m):
        l1.append(l[c])
        c+=1
    l2.append(l1)
print("\nThe right side way :")
for i in l2:
    for j in i:
        print(j,end=" ")
    print()
print("\nThe translated way :")
for i in range(n):
    for j in range(m):
        t1=(l2[i][j]//m)
        t2=(l2[i][j]%m)
        t3=(t1,t2)
        print(t3,end=" ")
    print()