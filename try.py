import mysql.connector,sys
mydb = mysql.connector.connect(host='localhost', user='root', passwd = '')
mycur=mydb.cursor()
mycur.execute("use example")
mycur.execute("describe adi123")
print(mycur.fetchall())