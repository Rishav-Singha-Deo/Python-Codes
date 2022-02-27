import random as rr
def tictactoe(l):
    while True:
        r=rr.randint(0,2)
        c=rr.randint(0,2)
        if l[r][c]==0:
            l[r][c]=2
            break
    return l
l=[[0,0,0],[0,0,0],[0,0,0]]
for i in l:
    for j in i:
        print("",j,end=" ")
    print()
tictactoe(l)
print("=========")
for i in l:
    for j in i:
        print("",j,end=" ")
    print()