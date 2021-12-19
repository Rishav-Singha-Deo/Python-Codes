s=input("Enter any string : ")
s=s.split(" ")
c=0
for i in s:
    i=i.replace(".","")
    i=i.replace(",","")
    i=i.replace("?","")
    i=i.replace("!","")
    i=i.replace(":","")
    i=i.replace(";","")
    i=i.replace('"',"")
    i=i.replace("'","")
    i=i.replace("-","")
    if i.isalpha()==True:
        c+=1
if c==0:
    print("There are no words in the string.")
elif c==1:
    print("There is only 1 word in the string.")
else:
    print("There are",c,"words in the string.")