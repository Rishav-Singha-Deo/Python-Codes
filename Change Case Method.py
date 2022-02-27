'''
Write a function called change_case that given a string, returns a
string with each upper case letter replaced by a lower case letter
and vice-versa.
'''
def change_case(s):
    s1=""
    for i in s:
        if i.isupper():
            s1+=i.lower()
        else:
            s1+=i.upper()
    return s1
s=input("Enter a string : ")
print("The required string :",change_case(s))