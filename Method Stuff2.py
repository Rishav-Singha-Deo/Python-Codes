'''
Develop an Python script with three component functions: main,
make_positive and make_negetive. The function main prompts the
user for a whole number and checks whether the whole number is
negative or positive. If the whole number is negative, main invokes
the function make_positive which multiplies the number by itself
and prints the result. If it is positive, main will invoke the function
make_negetive, which multiplies the number by itself, then by -1,
and prints the result.
'''
def make_positive(n):
    return n*n
def make_negative(n):
    return n*n*(-1)
def main():
    n=int(input("Enter an integer : "))
    if n>0:
        print("The result :",make_negative(n))
    if n<0:
        print("The result :",make_positive(n))
main()