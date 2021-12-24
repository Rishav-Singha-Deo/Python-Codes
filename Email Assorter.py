n=int(input("How many email addresses do you want to enter : "))
e=[]
sc,pc,ec=0,0,0
for i in range(n):
    print("Enter address number",(i+1),":",end=" ")
    t=input("")
    e.append(t)
for s in e:
    s=s.split("@")
    if s[1]=="student.tiu.edu":
        sc+=1
    elif s[1]=="prof.tiu.edu":
        pc+=1
    else:
        ec+=1
print("Students Addresses :",sc,"\nProfessors Addresses :",pc,"\nOther Addresses :",ec)