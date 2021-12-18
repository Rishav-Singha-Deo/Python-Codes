u=eval(input("Enter the upper limit : "))
l=eval(input("Enter the lower limit : "))
print("All the Abundant Numbers within this range :")
for i in range(l,u+1):
   f=[]
   for j in range(1,int(i/2)+1):
       if i%j==0:
           f.append(j)
   if sum(f)>i:
       print(i,end=", ")
