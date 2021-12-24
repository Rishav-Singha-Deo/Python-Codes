'''
Develop a Python script named showTable that takes a list of lists
of strings for
(a) Printing it in a well-organized table with each column right justified.
Assume that all the inner lists will contain the same
number of strings. For example, the value could look like this:
tableData = [[’Jasmine’, ’Rose, ’Tulip’, ’Chrysanthemum’],
[’Julia’, ’Jahanara’, ’Manasi’, ’Tapasi’],
[’is akin to’, ’resembles’, ’reminds me the name of’, ’is
another name for’]]
(b) Make sentences by combining each word from the second list
with the corresponding phrase in the second list followed by
the corresponding word from the first list.For example, the first
sentence would be: Julia is akin to Jasmin.
'''
r=int(input("Enter the number of inner lists : "))
c=int(input("Enter the number of strings in each inner list : "))
l=[["" for i in range(c)] for j in range(r)]
k=[["" for i in range(r)] for j in range(c)]
for i in range(r):
    for j in range(c):
        print("Enter the string number",j+1,"at inner list",i+1,":",end=" ")
        l[i][j]=input("")
for i in range(c):
    for j in range(r):
        k[i][j]=l[j][i]
print("The new sentences formed are as follows :")
for i in range(c):
    print(" ".join(k[i]),end=".\n")