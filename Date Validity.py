import datetime
d=input("Enter the date in dd/mm/yyyy : ")
dd,mm,yy=d.split('/')
c=1
try:
    datetime.datetime(int(yy), int(mm), int(dd))
except:
    c=0
if(c==1):
    print("Valid Date")
else:
    print("Invalid Date")