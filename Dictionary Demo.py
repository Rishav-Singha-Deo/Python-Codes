'''
Write a program that repeatedly asks the user to enter product
names and prices. Store all of these in a dictionary whose keys are
the product names and whose values are the prices. When the user
is done entering products and prices, allow them to repeatedly enter
a product name and print the corresponding price or a message if
the product is not in the dictionary.
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
print("\nPress 0 to stop")
print("Enter a product name to print it's price")
while True:
    print("=======================================")
    s=input("Enter the product name : ")
    if s in d:
        print("The price :",d[s])
    elif s=="0":
        break
    else:
        print("The product doesn't exist.")