u=eval(input("Enter the upper limit : "))
l=eval(input("Enter the lower limit : "))
def sum(n):
    s=0
    while(n!=0):
        s+=(n%10)
        n=n//10
    return s
print("All the Harshad Numbers within this range :")
for i in range(l,u+1):
    if i%sum(i)==0:
        print(i,end=", ")