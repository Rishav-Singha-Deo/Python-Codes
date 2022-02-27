l=[[1 if i%2==0 else 2 for i in range(8)] if j%2==0 else [2 if i%2==0 else 1 for i in range(8)] for j in range(8)]
print("The checkerboard pattern :")
for i in l:
    for j in i:
        print(j,end="  ")
    print()