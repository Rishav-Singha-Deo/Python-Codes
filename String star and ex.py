new_str=input("Enter a string : ")
if len(new_str)>=3:
    new_str=new_str[0:2]+"*"+new_str[3:]+"!!"
    print("The updated string is :",new_str)
else:
    print("The string is too short for this.")