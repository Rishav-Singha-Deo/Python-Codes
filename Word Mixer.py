s1=input("Enter two words of the same length.\nEnter the first word : ")
s2=input("Enter the second word : ")
s3=""
if len(s1)==len(s2):
    for i in range(len(s1)):
        s3=s3+s1[i]+s2[i]
    print("The new word is :",s3)
else:
    print("Both the words are not of the same length.")