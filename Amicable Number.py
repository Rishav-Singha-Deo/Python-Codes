u=int(input("Enter the upper limit : "))
l=int(input("Enter the lower limit : "))
print("The Amicable numbers in this range :")
for i in range(l,u+1):
    for j in range(i,u+1):
        s1,s2=0,0
        for k in range(1,i):
            if i%k==0:
                s1+=k
        for k in range(1,j):
            if j%k==0:
                s2+=k
        if s1==j and s2==i:
            print(i,"&",j,end=", ")