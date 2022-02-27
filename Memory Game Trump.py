import random
import time
l,o,s=[[random.randint(0,1) for i in range(5)] for j in range(5)],0,0
print("Memorize the following matrix for 10 seconds :")
for i in l:
    for j in i:
        if j==1:
            o+=1
        print(j,end="  ")
    print()
time.sleep(13);print("\n"*100)
print("Now try to remember the positions of all the 1s in the matrix")
for i in range(o):
    print("Enter the row and columns :")
    r=int(input("Row : "))
    c=int(input("Column : "))
    if l[r-1][c-1]==1:
        l[r-1][c-1]=2
        s+=1
        print("HIT!")
    elif l[r-1][c-1]==2:
        print("Already attempted!")
    else:
        print("MISS!")
print("Your score is :",s,"out of",o)