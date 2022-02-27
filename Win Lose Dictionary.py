print("Enter 999 to stop")
d={}
while True:
    t=input("Enter the Team name : ")
    if t=="999":
        print("Stopped taking inputs")
        break
    w=int(input("Enter the no.of wins : "))
    l=int(input("Enter the no.of loses : "))
    print("==============================================")
    d[t]=[w,l]
print("==============================================")
t=input("Enter a team name : ")
if t in d:
    print("The winning percentage :",str(100*d[t][0]/(d[t][0]+d[t][1]))+"%")
else:
    print("Invalid input.")
print("==============================================")
w=[]
for i in d:
    w.append(d[i][0])
print("The list with all the wins :",w)
print("==============================================")
w=[]
for i in d:
    if d[i][0]>d[i][1]:
        w.append(i)
print("The Teams that has winning records :-")
for i in w:
    print(i)
print("==============================================")