import pymysql

db = pymysql.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'root', 
    database = 'laplateforme'
    )

cursor = db.cursor()

req = 'select * from etudiants'

cursor.execute(req)
datas = cursor.fetchall()

print(datas)
cursor.close()