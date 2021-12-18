items = []
quant = []
price = []
sum=0
while True:
    c=eval(input("1. Add item\n2. Calculate bill\nEnter you choice : "))
    if c==1:
        i=input("Enter the item's name : ")
        q=eval(input("Enter the item's quantity : "))
        p=eval(input("Enter the item's price : "))
        p=p*q
        sum=sum+p
        items.append(i)
        quant.append(q)
        price.append(p)
    elif c==2:
        print("*********************BILL*********************\nItem Name\t\tItem Quantity\t\tItem Price")
        for i in range(len(items)):
            print(items[i],"\t\t\t\t",quant[i],"\t\t\t\t\t",price[i])
        print("**********************************************""\nTotal Amount to be paid : ₹",sum,"\n**********************************************")
        break