p=eval(input("Enter the Principal Amount : "))
r=eval(input("Enter the Rate of Annual Interest : "))
n=eval(input("Enter the number of Months : "))
r=r/12/100
e=p*r*((1+r)**n)/(((1+r)**n)-1)
print("The EMI is : ",e)