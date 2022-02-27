def win_check(l):
    sr=list(map(sum,l))
    sc=list(map(sum,zip(*l)))
    sd1,sd2=0,0
    for i in range(3):
        sd1+=l[i][i]
        sd2+=l[i][2-i]
    if 6 in sr or 6 in sc:
        return True
    if sd1==6 or sd2==6:
        return True
l=[[2,0,0],
   [0,2,0],
   [0,0,2]]
print(win_check(l))