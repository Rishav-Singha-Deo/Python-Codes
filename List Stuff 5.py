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