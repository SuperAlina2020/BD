# work_with_BD
import sqlite3
import pprint

connection = sqlite3.connect('test1.db')
cursor = connection.cursor()

#sql_command = """CREATE TABLE salary(
#staff_id INTEGER PRIMARY KEY,
#full_name varchar(20),
#staff_salary INTEGER(20),
#join_date DATE);"""
#cursor.execute(sql_command)
#cursor.execute("INSERT INTO salary VALUES(1,'Baistan',30000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(2,'Alina',100000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(3,'Erjan',50000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(4,'Maksim',100,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(5,'Misha',51000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(6,'Fil',32000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(7,'Ivan',101000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(8,'Evgene',60000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(9,'Lisa',38000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(10,'Danil',73000,'2020-10-10')")
#cursor.execute("INSERT INTO salary VALUES(11,'Sasha',130000,'2020-10-10')")

cursor.execute("SELECT * FROM salary WHERE staff_salary>=80000;")
ans = cursor.fetchall()
pprint.pprint(ans)

connection.commit()
connection.close()
