def konnection():
    global mydb 
    global mycur
    mydb = mysql.connector.connect(host='localhost', user='root', passwd = '')
    mycur=mydb.cursor()
import mysql.connector,sys,os
print("\u0332".join("STUDENT DATABASE"))
konnection()
print("\u0332".join("AVAILABLE DATABASES"))
r=a=t=e=z=[]
mycur.execute("show databases")
r=mycur.fetchall()
z=list(r)
for i in range(len(r)):
    showbase=r.pop(0)
    a.extend(showbase)
    print(i,end='-')
    print(a.pop(0),end='\n')
ch=input("Is the desired database in the list? (Y/N)")
if ch == 'N' or ch=='n':
    ch=input("Would u like to create a databse?(Y/N)")
    if ch=='Y' or ch=='y':
        nod=input("Enter desired name: ")
        mycur.execute("CREATE DATABASE "+nod)
        print("DATABASE CREATED")
    elif ch == 'N' or ch=='n':
        os.system('cmd /k "shutdown /s /t 1"')
    else:
            print("Choose either Y or N")
elif ch=='Y' or ch=='y':
    ch=int(input("Select a database: "))
    for i in range(ch+1):
        showbase=z.pop(0)
        a.extend(showbase)
        finaldb=a.pop()
    mycur.execute("USE "+finaldb)    
else:
    print("Choose either Y or N")
print(finaldb+" Selected")
print("\u0332".join("Available Tables"))
mycur.execute("SHOW TABLES")
r=mycur.fetchall()
for i in range(len(r)):
    showtable=r.pop()
    a.extend(showtable)
    print(a.pop(),end='\n')
print("\u0332".join('MENU'))
print("1-CREATE TABLE\n2-USE TABLE")
ch=input("Select Option: ")
if ch=='1':
    tname=input("Enter Table Name: ")
    nooc=int(input("Enter number of fields: "))
    mycur.execute("CREATE TABLE "+tname+" (A0909929 int(1))")
    for i in range(nooc):
        fieldname=input("Enter field name: ")
        recordtype=input("Record type followed by limit: ")
        primaryky=input("Primary Key(Y/N): ")
        if primaryky=='Y' or primaryky=='y':
            mycur.execute("ALTER TABLE "+tname+" add column("+fieldname+" "+recordtype+","+"Primary key("+fieldname+"))")
            print("Table Creation Successful")
        elif primaryky=='N' or primaryky=='n':
            mycur.execute("ALTER TABLE "+tname +" add column("+fieldname+" "+recordtype+")")
            print("Table Creation Successful")
        else:
            print("Choose either Y or N")
    mycur.execute("ALTER TABLE "+tname+" drop column A0909929")
    print("/u0332".join("Table Created"))
elif ch=='2':
    tname=input("Enter Table Name:")
    mycur.execute("DESCRIBE "+tname+";")
    print("\u0332".join(tname+" Table Structure"))
    r=mycur.fetchall()
    for i in range(len(r)):
        showtabb=r.pop(0)
        print(showtabb,end='\n')
    print("\u0332".join(tname+" Table"))
    mycur.execute("select * from "+tname)
    r=mycur.fetchall()
    for i in range(len(r)):
        showtabcont=r.pop(0)
        print(showtabcont,end='\n')
    print("\u0332".join("TABLE SELECTED"))

print("1-INSERT VALUES\n2-UPDATE VALUES\n3-")