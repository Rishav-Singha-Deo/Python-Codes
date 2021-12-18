import datetime
y=input("Enter the year : ")
print("The following month(s) have Friday th 13th :")
for i in range(1,13):
    if datetime.datetime.strptime('13 '+' '+str(i)+' '+y,'%d %m %Y').weekday()==4:
        print(datetime.date(int(y),(i),13).strftime('%B'))