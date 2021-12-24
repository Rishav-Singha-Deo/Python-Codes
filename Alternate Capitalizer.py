s=input("Enter any word : ")
print("The required word is :",end=" ")
for i in range(0,len(s)-1,2):
    print("%s%s"%(s[i],s[i+1].upper()),end="")