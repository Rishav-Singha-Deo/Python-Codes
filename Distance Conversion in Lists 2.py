print("Available units are"
      "\nInch\tYard\tMile\tMillimeter"
      "\nCentimeter\tMeter\tKilometer")
n=eval(input("Enter any length : "))
u=input("Enter the unit of this length : ").lower()
c=input("Enter the unit you want to convert to : ").lower()
l=[["inch","yard","mile","millimeter","centimeter","meter","kilometer"],
   [n,n*0.0277777778,n*0.0000157828,n*25.4,n*2.54,n*0.0254,n*0.0000254],
   [n*36,n,n*0.0005681818,n*914.4,n*91.44,n*0.9144,n*0.0009144],
   [n*63360,n*1760,n,n*1609344,n*160934.4,n*1609.344,n*1.609344],
   [n*0.0393700787,n*0.0010936133,n*0.00000062137,n,n*0.1,n*0.001,n*0.000001],
   [n*0.3937007874,n*0.010936133,n*0.0000062137,n*10,n,n*0.01,n*0.00001],
   [n*39.37007874,n*1.0936132983,n*0.0006213712,n*1000,n*100,n,n*0.001],
   [n*39370.07874,n*1093.6132983,n*0.6213711922,n*1000000,n*100000,n*1000,n]]
id1=l[0].index(u)
id2=l[0].index(c)
print("The converted value is :",l[id1+1][id2],l[0][id2],end="(s)")