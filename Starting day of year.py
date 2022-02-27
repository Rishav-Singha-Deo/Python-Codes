from calendar import monthrange
y=eval(input("Enter any year : "))
d=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
w,m=monthrange(y,1)
print(d[int(w)])