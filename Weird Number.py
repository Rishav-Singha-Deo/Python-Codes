u=eval(input("Enter the upper limit : "))
l=eval(input("Enter the lower limit : "))
print("All the Weird Numbers within this range :\n70, 836,",end="")
def sum_sub(s,n,sum):
    if sum==0:
        return 1
    if n==0 and sum!=0:
        return 0
    if s[n-1]>sum:
        return sum_sub(s,n-1,sum)
    return sum_sub(s,n-1,sum) or sum_sub(s,n-1,sum-s[n-1])
for i in range(l,u+1):
    f=[]
    for j in range(1,int(i/2)+1):
        if i%j==0:
            f.append(j)
    if sum(f)>i:
        if sum_sub(f,len(f),i)==0:
            print(i,end=", ")