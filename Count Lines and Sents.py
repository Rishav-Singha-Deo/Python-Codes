s="""Hello. How are you?
What did you ask? Oh, my name!
My name is Guido. What is your name?
Alas! You cannot answer that, can you?"""
print("The string is :\n%s"%s)
p=s.count(".")
q=s.count("?")
e=s.count("!")
print("The number of sentence(s) :",(p+q+e))
s=s.split("\n")
print("The number of line(s) :",len(s))
