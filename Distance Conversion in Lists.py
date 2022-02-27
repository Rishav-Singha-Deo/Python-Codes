n=eval(input("Enter any distance in feet : "))
print("Press the number to convert\n1. Inches\n2. Yards\n3. Miles\n"
      "4. Millimeters\n5. Centimeters\n6. Meters\n7. Kilometers")
l1=[0,n*12,n*(1/3),n*0.000189394,n*304.8,n*30.48,n*0.3048,n*0.0003048]
l2=["","Inches","Yards","Miles","Millimeters","Centimeters","Meters","Kilometers"]
c=int(input("Enter choice : "))
print(n,"Feets =",l1[c],l2[c])