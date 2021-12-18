r=eval(input("Rows : "))
c=eval(input("Cols : "))
a=[[0]*c for i in range(r)]
for i in range(0,r):
    for j in range(0,c):
        a[i][j]=eval(input(": "))
cl=list(zip(*a))
print(cl[1])
print(a[1])