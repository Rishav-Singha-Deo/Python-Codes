l=[1,2,3,4,5,6,7,8,9]
for i in l:
    print(i,end="  ")
print("\n")
l=[l[i:i+3] for i in range(0,len(l),3)]
for i in l:
    for j in i:
        print(j,end="  ")
    print()