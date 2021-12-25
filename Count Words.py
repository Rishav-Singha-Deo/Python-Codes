s=input("Enter any string : ")
s=s.split(" ")
c=0
for i in s:
    if i[0].isalpha():
        c+=1
if c==0:
    print("There are no words in the string.")
elif c==1:
    print("There is only 1 word in the string.")
else:
    print("There are",c,"words in the string.")
