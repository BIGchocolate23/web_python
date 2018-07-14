import mysql.connector
conn = mysql.connector.connect(user='root', password='shangxiaonan23', database='test')
cursor = conn.cursor()