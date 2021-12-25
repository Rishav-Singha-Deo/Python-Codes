s=input("Enter any formula : ")
s=s.split("=")
if s[0].count("(")>s[0].count(")"):
    print("You have unclosed parentheses in LHS.")
if s[1].count("(")>s[1].count(")"):
    print("You have unclosed parentheses in RHS.")
if s[0].count("(")<s[0].count(")"):
    print("You have unopened parentheses in LHS.")
if s[1].count("(")<s[1].count(")"):
    print("You have unopened parentheses in RHS.")
if s[0].count("(")==s[0].count(")") and s[1].count("(")==s[1].count(")"):
    print("The parentheses are okay.")
