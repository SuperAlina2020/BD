# work_with_BD
import sqlite3
from pprint import pprint

connection = sqlite3.connect('test.db')

cursor = connection.cursor()
#
# sql_command = '''CREATE TABLE products(
# product_id INTEGER PRIMARY KEY,
# product_name varchar(20),
# product_description varchar(50),
# customer varchar(20),
# pub_date DATE);'''

#
# sql_command = """INSERT INTO products values(5,'IPHONE 12 Pro Max','No comment',
# 'Danil','2020-10-19');"""
# cursor.execute(sql_command)

cursor.execute("SELECT * FROM salary LIMIT 2;")

ans = cursor.fetchall()
pprint(ans)
connection.commit()
connection.close()