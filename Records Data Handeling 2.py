'''
Develop a Python script to create a text file to write the records
of employees of a company comprising EMP-ID,EMP-Name,Deptt
and Basic Pay and then to create another file containing salary data
of all the employees with the following specifications:
    •Each salary record will consist of EMP-ID,EMP-Name,Deptt
        ,Basic Pay,DA,MA,HRA,Gross-Pay,PF,PT,IT and Net-Pay.
    • DA is calculated @109% of the basic pay subject to minimum
        of Rs. 10000.
    • MA is calculated @21% of basic pay subject to a minimum of
        Rs.3000 and a maximum of Rs.7000.
    • HRA is calculated @35% of the basic pay subject to a maximum
        of Rs.20,000.
    • Gross-Pay is the sum of Basic Pay,DA,MA,HRA.
    • PT is Rs. 100 for employees having Gross-Pay <50000, otherwise,
        it is Rs. 200.
    • PF is 12.5% of the Gross-Pay
    • IT is calculated @10% for having the Gross-Pay that exceeds
        70,000 but less than 100,000;otherwise, it is 20% of the Gross-
        Pay.
    • Net Pay is calculated by subtracting PF,PT and IT from the
        Gross-Pay.
    • Show the names of the employees in abbreviated form like Amal
        Kumar Biswas as A.K. Biswas
    • Format the Net-pay rounded to nearest rupees by taking the
        upper value.
'''
from tabulate import tabulate
import numpy
colname1=["EMP-ID","EMP-Name","Deptt","Basic Pay"]
colname2=["EMP-ID","EMP_Name","Deptt","Basic Pay","DA","MA","HRA","Gross-Pay","PF","PT","IT","Net-Pay"]
l1,l2,empid,empname,abv,deptt,bp,da,ma,hra,gp,pf,pt,it,np=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
print("Enter 999 in employee id to stop entering")
while True:
    print("================================")
    e=input("Enter the Employee ID : ")
    if e=="999":
        break
    empid.append(e)
    empname.append(input("Enter the Employee name : "))
    l=empname[-1].split()
    tmp=""
    for i in range(len(l)-1):
        s=l[i]
        tmp+=(s[0].upper()+". ")
    tmp+=l[-1].title()
    abv.append(tmp)
    deptt.append(input("Enter the department : "))
    bp.append(int(input("Enter the basic pay : ")))
    tmp=bp[-1]*(109/100)
    if tmp<10000:
        da.append(10000)
    else:
        da.append(tmp)
    tmp=bp[-1]*(21/100)
    if tmp<3000:
        ma.append(3000)
    elif tmp<7000:
        ma.append(7000)
    else:
        ma.append(tmp)
    tmp=bp[-1]*(35/100)
    if tmp>20000:
        hra.append(20000)
    hra.append(tmp)
    gp.append(bp[-1]+da[-1]+ma[-1]+hra[-1])
    pf.append(gp[-1]*(12.5/100))
    if gp[-1]<50000:
        pt.append(100)
    else:
        pt.append(200)
    if gp[-1]>70000 and gp[-1]<100000:
        it.append(gp[-1]*(10/100))
    else:
        it.append(gp[-1]*(20/100))
    np.append(round((gp[-1]-pf[-1]-pt[-1]-it[-1])+0.5))
l1.append(empid);l1.append(empname);l1.append(deptt);l1.append(bp)
l2.append(empid);l2.append(abv);l2.append(deptt);l2.append(bp);l2.append(da);l2.append(ma)
l2.append(hra);l2.append(gp);l2.append(pf);l2.append(pt);l2.append(it);l2.append(np)
data=numpy.array(l1)
datat=data.T.tolist()
print("================================")
print("The records are as follows :")
print(tabulate(datat,headers=colname1,tablefmt="grid"))
file=open("Records.txt","x")
file.write(tabulate(datat,headers=colname1,tablefmt="grid"))
data=numpy.array(l2)
datat=data.T.tolist()
print("================================")
print("The records are as follows :")
print(tabulate(datat,headers=colname2,tablefmt="grid"))
file=open("Salary Data.txt","x")
file.write(tabulate(datat,headers=colname2,tablefmt="grid"))
'''
Enter 999 in employee id to stop entering
================================
Enter the Employee ID : 6546
Enter the Employee name : Gregory Greg House
Enter the department : Diagnostics
Enter the basic pay : 15000
================================
Enter the Employee ID : 8284
Enter the Employee name : James Evan Wilson
Enter the department : Oncology
Enter the basic pay : 17000
================================
Enter the Employee ID : 9803
Enter the Employee name : Lisa Edelstein Cuddy
Enter the department : Administration
Enter the basic pay : 21000
================================
Enter the Employee ID : 999
================================
The records are as follows :
+----------+----------------------+----------------+-------------+
|   EMP-ID | EMP-Name             | Deptt          |   Basic Pay |
+==========+======================+================+=============+
|     6546 | Gregory Greg House   | Diagnostics    |       15000 |
+----------+----------------------+----------------+-------------+
|     8284 | James Evan Wilson    | Oncology       |       17000 |
+----------+----------------------+----------------+-------------+
|     9803 | Lisa Edelstein Cuddy | Administration |       21000 |
+----------+----------------------+----------------+-------------+
================================
The records are as follows :
+----------+--------------+----------------+-------------+-------+------+-------+-------------+------+------+-------+-----------+
|   EMP-ID | EMP_Name     | Deptt          |   Basic Pay |    DA |   MA |   HRA |   Gross-Pay |   PF |   PT |    IT |   Net-Pay |
+==========+==============+================+=============+=======+======+=======+=============+======+======+=======+===========+
|     6546 | G. G. House  | Diagnostics    |       15000 | 16350 | 7000 |  5250 |       43600 | 5450 |  100 |  8720 |     29330 |
+----------+--------------+----------------+-------------+-------+------+-------+-------------+------+------+-------+-----------+
|     8284 | J. E. Wilson | Oncology       |       17000 | 18530 | 7000 |  5950 |       48480 | 6060 |  100 |  9696 |     32624 |
+----------+--------------+----------------+-------------+-------+------+-------+-------------+------+------+-------+-----------+
|     9803 | L. E. Cuddy  | Administration |       21000 | 22890 | 7000 |  7350 |       58240 | 7280 |  200 | 11648 |     39112 |
+----------+--------------+----------------+-------------+-------+------+-------+-------------+------+------+-------+-----------+

Process finished with exit code 0

'''