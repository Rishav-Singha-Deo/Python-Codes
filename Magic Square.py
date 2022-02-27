l=[[5,6,19,68],[69,18,3,8],
   [4,7,70,17],[20,67,6,5]]
print("The Matrix :")
for i in l:
    print(i)
s1,s2=0,0
for i in range(4):
    s1+=l[i][i]
    s2+=l[i][3-i]
for i in range(4):
    s3,s4=0,0
    for j in range(4):
        s3+=l[i][j]
        s4+=l[j][i]
    if not(s1==s2==s3==s4):
        print("\nNot Magic Square")
        exit()
print("\nMagic Square")