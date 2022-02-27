l=[]
for i in range(12):
    l1=[0 for j in range(1,i)]
    l.extend(l1)
    l.append(1)
print(l)