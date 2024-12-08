#ASOMA STEEL WORKS INVENTORY MANAGEMENT
import mysql.connector
AsomaDB = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ogiecy9856",
  database="users"
)
#print(AsomaDB)
cursor = AsomaDB.cursor()
#cursor.execute(CREATE DATABASE 'ASWdatabase')
#cursor.execute('CREATE TABLE  Pipe (name VARCHAR(20), Inches VARCHAR(10))')
#cursor.execute('ALTER TABLE pipe ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
sql = 'INSERT INTO pipe (name, Inches) VALUES (%s, %s)'
val = ('DrilllingPipe', '20inches')
cursor.execute(sql, val)
AsomaDB.commit()# it is required to make changes otherwise no changes are made to table
print(cursor.rowcount)
#cursor.execute('CREATE DATABASE users')
cursor.execute("CREATE TABLE ")
