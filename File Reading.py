'''
Develop a Python script to read an existing text file to print line
number of each line and the number of words in the line in a tabular
format.Finally,the script prints the total number of lines in the file
and and the total number of words.

Make a txt file in the same folder and name it "Test.txt"
'''
from tabulate import tabulate
file=open("Test.txt","r")
l,ln,wd=[],0,0
content=file.read()
colist=content.split("\n")
for i in range(len(colist)):
    c=0
    k=colist[i].split(" ")
    for j in k:
        if j:
            c+=1
            wd+=1
    ln+=1
    l.append([i+1,c])
print(tabulate(l,headers=["Line No.","No. of Words"],tablefmt="grid"))
print("There are",ln,"lines and",wd,"words in the file")
'''
INPUT:
Hello, my name is Sir Patrick Stewart.
You may know me from various franchises.
Such as the Star Trek and the X men.
I am supposed to be in the new MCU film.
Thank you for listening!

OUTPUT:
+------------+----------------+
|   Line No. |   No. of Words |
+============+================+
|          1 |              7 |
+------------+----------------+
|          2 |              7 |
+------------+----------------+
|          3 |              9 |
+------------+----------------+
|          4 |             10 |
+------------+----------------+
|          5 |              4 |
+------------+----------------+
There are 5 lines and 37 words in the file

Process finished with exit code 0

'''