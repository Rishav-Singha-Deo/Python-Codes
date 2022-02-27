def swap_val(x,y,z):
    z=x+y+z
    y=z-y-x
    x=z-y-x
    z=z-y-x
    return x,y,z
x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
z=int(input("Enter the value of z : "))
print("\nBefore swapping:-")
print("x :",x,"\ty :",y,"\tz :",z)
x,y,z=swap_val(x,y,z)
print("\nAfter swapping:-")
print("x :",x,"\ty :",y,"\tz :",z)