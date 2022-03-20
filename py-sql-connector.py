def konnection():
    global mydb 
    global mycur
    mydb = mysql.connector.connect(host='localhost', user='root', passwd = '1234')
    mycur=mydb.cursor()
import mysql.connector,sys,os
print("\u0332".join("STUDENT DATABASE\n"))
konnection()
print("\u0332".join("AVAILABLE DATABASES\n"))
r=a=t=e=z=temp2=fieldn=[]
mycur.execute("show databases")
r=mycur.fetchall()
z=list(r)
for i in range(len(r)):
    showbase=r.pop(0)
    a.extend(showbase)
    print(i,end='-')
    print(a.pop(0),end='\n')
ch=input("\nIs the desired database in the list? (Y/N)")
if ch.upper() == 'Y':
    ch=int(input("\nSelect a database: "))
    for i in range(ch+1):
        showbase=z.pop(0)
        a.extend(showbase)
        finaldb=a.pop()
    mycur.execute("USE "+finaldb)    
    print(finaldb+" Selected")
    print("\u0332".join("\nAvailable Tables"))
    mycur.execute("SHOW TABLES")
    r=mycur.fetchall()
    for i in range(len(r)):
        showtable=r.pop()
        a.extend(showtable)
        print(a.pop(),end='\n')
elif ch.upper() == 'N':
    ch=input("\nWould u like to create a databse?(Y/N)\n")
    if ch.upper() == 'Y':
        nod=input("Enter desired name: ")
        print()
        mycur.execute("CREATE DATABASE "+nod)
        print("DATABASE CREATED")
        mycur.execute("Use"+nod)
        print(nod+" Selected")
    elif ch.upper() == 'N':
        os.system('cmd /k "shutdown /s /t 1"')
    else:
        print("Choose either Y or N")   
else:
    print("\nChoose either Y or N\n")
print()
print("\u0332".join('MENU'))
print("1-CREATE TABLE\n2-USE TABLE\n3-ALTER TABLE")
ch=input("\nSelect Option: ")
if ch=='1':
    tname=input("Enter Table Name: ")
    nooc=int(input("Enter number of fields: "))
    mycur.execute("CREATE TABLE "+tname+" (A0909929 int(1))")
    for i in range(nooc):
        print()
        print("\u0332".join(i))
        fieldname=input("Enter field name: ")
        recordtype=input("Record type followed by size: ")
        primaryky=input("Primary Key(Y/N): ")
        if primaryky.upper()=='Y':
            mycur.execute("ALTER TABLE "+tname+" add column("+fieldname+" "+recordtype+","+"Primary key("+fieldname+"))")
        elif primaryky.upper()=='N':
            mycur.execute("ALTER TABLE "+tname +" add column("+fieldname+" "+recordtype+")")
        else:
            print("\nChoose either Y or N")
    mycur.execute("ALTER TABLE "+tname+" drop column A0909929")
    print("/u0332".join("Table Created"))
elif ch=='2':
    tname=input("\nEnter Table Name:")
    mycur.execute("DESCRIBE "+tname+";")
    print()
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
elif ch=='3':
    print("incomplete code")

print("\u0332".join('\nMENU'))
print("1-INSERT VALUES\n2-UPDATE VALUES\n3-DELETE ROW\n")
ch=input("Select Option: ")

if ch=='1':
    mycur.execute("describe students")
    tabledes=mycur.fetchall()
    for i in range(len(tabledes)):
        fieldnum=tabledes.pop(0)
        temp2.extend(fieldnum)
        print(temp2.pop(0),end=" ")
        for i in range (len(temp2)):
            temp2.pop()
    print()
    ch=input("Enter Values: ")
    mycur.execute("Insert into "+tname+" values("+ch+")")
    mydb.commit()
    print("\u0332".join("Record inserted"))
elif ch=='2':
    mycur.execute("select * from "+tname)
    r=list[mycur.fetchall()]
    for i in range(len(r)):
        indtabdes=r[i]
        tabfield=indtabdes[0]
        fieldn.append(tabfield)
        tupfield=tuple(fieldn)
    print(tupfield)
    vals=tuple(input("Enter Values: "))
    mycur.execute("Update "+tname+" ("+tupfield+") values"+vals)
    mydb.commit()
elif ch=='3':
    mycur.execute("select * from "+tname)
    r=list[mycur.fetchall()]
    for i in range(len(r)):
        indtabdes=r[i]
        tabfield=indtabdes[0]
        fieldn.append(tabfield)
        tupfield=tuple(fieldn)
    print(tupfield)
    vals=tuple(input("Enter Values: "))
    mycur.execute("delete from "+tname+" ("+tupfield+") values"+vals)
    mydb.commit()