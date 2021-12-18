a=[[20,15,18,20,25],
   [18,20,12,14,15],
   [21,23,25,27,25],
   [17,18,21,23,20],
   [18,18,16,19,20]]
cl=list(zip(*a))
r=[[0]*len(cl) for i in range(len(a))]
c=[[0]*len(cl) for i in range(len(a))]
print("Row wise Subtraction")
for i in range(len(a)):
    m=min(a[i])
    for j in range(len(cl)):
        r[i][j]=a[i][j]-m
for i in range(len(r)):
    print(r[i])
print("Column wise Subtraction")
for i in range(len(cl)):
    m=min(cl[i])
    for j in range(len(a)):
        c[j][i]=cl[i][j]-m
for i in range(len(r)):
    print(c[i])