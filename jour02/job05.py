import pymysql

db = pymysql.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'root', 
    database = 'laplateforme'
    )

cursor = db.cursor()

req = 'SELECT sum(superficie) from etage'

cursor.execute(req)
datas = cursor.fetchone()[0]
print(f'La superficie de La Plateforme est de {datas} m²')
cursor.close()