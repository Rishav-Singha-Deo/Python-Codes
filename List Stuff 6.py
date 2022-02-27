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