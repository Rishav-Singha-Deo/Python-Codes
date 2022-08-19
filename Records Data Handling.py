'''
Develop a Python script to create a text file to write the records of
employees of a company comprising EMP-ID,EMP-Name,Deptt,Dateof-
Joining and Date-Of-birth to determine and print EMP-ID,EMPName,
Deptt.Years-served and Age-on-01-01-2023 for those employees
who will either complete 60 years in age or 40 years in service.
Assume that the dates are in mm-dd-yyyy format.
'''
from tabulate import tabulate
import numpy
colname1=["EMP-ID","EMP-Name","Deptt","Date-of-Joining","Date-Of-Birth"]
colname2=["EMP-ID","EMP_Name","Deptt","Years-served","Age-on-01-01-2023"]
l1,l2,empid,empname,deptt,doj,dob=[],[],[],[],[],[],[]
print("Enter 999 in employee id to stop entering")
while True:
    print("================================")
    e=input("Enter the Employee ID : ")
    if e=="999":
        break
    empid.append(e)
    empname.append(input("Enter the Employee name : "))
    deptt.append(input("Enter the department : "))
    doj.append(input("Enter the date of joining : "))
    dob.append(input("Enter the date of birth : "))
l1.append(empid);l1.append(empname);l1.append(deptt);l1.append(doj);l1.append(dob)
data=numpy.array(l1)
datat=data.T.tolist()
print("================================")
print("The records are as follows :")
print(tabulate(datat,headers=colname1,tablefmt="grid"))
file=open("records1.txt","x")
file.write(tabulate(datat,headers=colname1,tablefmt="grid"))
for i in datat:
    if int(i[3][-4:])<1982 or int(i[4][-4:])<1962:
        i[3]=2023-int(i[3][-4:])
        i[4]=2023-int(i[4][-4:])
        l2.append(i)
    else:
        i.clear()
print("\nThe records of the required employees are as follows :")
print(tabulate(l2,headers=colname2,tablefmt="grid"))
file=open("records2.txt","x")
file.write(tabulate(l2,headers=colname2,tablefmt="grid"))
'''
Enter 999 in employee id to stop entering
================================
Enter the Employee ID : 6446
Enter the Employee name : Gregory House
Enter the department : Diagnostics
Enter the date of joining : 11-05-1989
Enter the date of birth : 01-09-1975
================================
Enter the Employee ID : 9932
Enter the Employee name : Elizabeth Cuddy
Enter the department : Dean of Medicine
Enter the date of joining : 09-15-1987
Enter the date of birth : 06-08-1960
================================
Enter the Employee ID : 3903
Enter the Employee name : James Wilson
Enter the department : Oncology
Enter the date of joining : 10-24-1981
Enter the date of birth : 01-04-1964
================================
Enter the Employee ID : 999
================================
The records are as follows :
+----------+-----------------+------------------+-------------------+-----------------+
|   EMP-ID | EMP-Name        | Deptt            | Date-of-Joining   | Date-Of-Birth   |
+==========+=================+==================+===================+=================+
|     6446 | Gregory House   | Diagnostics      | 11-05-1989        | 01-09-1975      |
+----------+-----------------+------------------+-------------------+-----------------+
|     9932 | Elizabeth Cuddy | Dean of Medicine | 09-15-1987        | 06-08-1960      |
+----------+-----------------+------------------+-------------------+-----------------+
|     3903 | James Wilson    | Oncology         | 10-24-1981        | 01-04-1964      |
+----------+-----------------+------------------+-------------------+-----------------+

The records of the required employees are as follows :
+----------+-----------------+------------------+----------------+---------------------+
|   EMP-ID | EMP_Name        | Deptt            |   Years-served |   Age-on-01-01-2023 |
+==========+=================+==================+================+=====================+
|     9932 | Elizabeth Cuddy | Dean of Medicine |             36 |                  63 |
+----------+-----------------+------------------+----------------+---------------------+
|     3903 | James Wilson    | Oncology         |             42 |                  59 |
+----------+-----------------+------------------+----------------+---------------------+

Process finished with exit code 0
'''