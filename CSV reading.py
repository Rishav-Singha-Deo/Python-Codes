'''
An excel data file contains 5 sheets of data about the students of five
different classes. Develop a Python script to read each of the sheets
in different .csv files to print total number of students,number of
boys,number of girls, average age of the boys and average age of
the girls for each of the classes by assuming any data structure you
deem suitable.
'''
import pandas as pd
st,genM,genF,listM,listF=0,0,0,[],[]
df=pd.concat(map(pd.read_csv,['st1.csv','st2.csv','st3.csv','st4.csv','st5.csv']),ignore_index=True)
for i in df.index:
    st+=1
for j in df.index:
    if df['Gender'][j]=='M':
        genM+=1
        listM.append(df['Age'][j])
    else:
        genF+=1
        listF.append(df['Age'][j])
print("Total no. of students :",st)
print("No. of boys :",genM)
print("No. of girls :",genF)
print("Average age of Boys :",sum(listM)/genM)
print("Average age of Girls :",sum(listF)/genF)
'''
INPUT :
st1
Roll No	Name	Gender	Age
1	    Rambo	M	    15
2	    Parwal	M	    16
3	    Jesal	M	    13
4	    Hetal	F	    14
5	    Netal	F	    15
6   	Kuntal	F	    14
7	    Puntal	M	    16

st2
Roll No	Name	Gender	Age
1	    Pari	F	    14
2	    Hari	M	    15
3	    Anadi	M	    14
4	    Khiladi	F	    15
5	    Gulabi	F	    16

st3
Roll No	Name	Gender	Age
1	    Puja	F	    16
2	    Ahuja	M	    16
3	    Manja	F	    15
4	    Panja	M	    14
5	    Hanja	M	    14
6	    Ganja	F	    16

st4
Roll No	Name	    Gender	Age
1	    Parminder	F	    14
2	    Joginder	F	    16
3	    Surrinder	M	    14
4	    Harinder	M	    15
5	    Grinder 	M	    15
6	    Binder	    M	    15
7	    Tinder	    F	    16

st5
Roll No	Name	Gender	Age
1	    Som	    M	    14
2	    Nath	M	    16
3	    Majum	F	    14
4	    Daar	M	    15
5	    Hori	F	    15

OUTPUT :
Total no. of students : 30
No. of boys : 16
No. of girls : 14
Average age of Boys : 14.8125
Average age of Girls : 15.0

Process finished with exit code 0

'''