def leapcheck(y):
    if (y%400==0) and (y%100==0):
        return 1
    elif (y%4==0) and (y%100!=0):
        return 1
    else:
        return 0
y=int(input("Enter a year : "))
if leapcheck(y)==1:
    print("Leap year")
else:
    print("Not leap year")