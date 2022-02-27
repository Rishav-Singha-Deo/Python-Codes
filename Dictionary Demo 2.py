'''
Write a program that repeatedly asks the user to enter product
names and prices. Store all of these in a dictionary whose keys are
the product names and whose values are the prices. When the user
is done entering products and prices, allow the user to enter a
dollar amount and print out all the products whose price is less
than that amount.
'''
d={}
print("Press 0 to stop")
while True:
    print("=======================================")
    s=input("Enter a product : ")
    if s=="0":
        break
    d[s]=int(input("Enter the price : "))
print("=======================================")
print("Enter a product name to print it's price")
n=int(input("Enter the dollar amount : "))
print("The following items' prices are less than",n,":-")
print("=======================================")
for i in d:
    if d[i]<n:
        print("Item name :",i,"\nPrice :",d[i])
        print("=======================================")