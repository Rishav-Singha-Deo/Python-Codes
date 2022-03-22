P=23
G=9
print("The Value of P is :",P)
print("The Value of G is :",G)
a=4
print("The Private Key a for Alice is :",a)
x=int(pow(G,a,P))
b=3
print("The Private Key b for Bob is :",b)
y=int(pow(G,b,P))
ka=int(pow(y,a,P))
kb=int(pow(x,b,P))
print("Secret key for the Alice is :",ka)
print("Secret Key for the Bob is :",kb)