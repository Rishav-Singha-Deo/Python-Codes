from time import time
min=eval(input("Enter the lower range : "))
max=eval(input("Enter the upper range : "))
print("The random number within the range is : ",int(((time()%10)/10)*(max-min+1)+min))