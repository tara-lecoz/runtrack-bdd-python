import pymysql

class Employes:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def connect(self):
        self.db = pymysql.connect(
            host = self.host, 
            user = self.user, 
            password = self.password, 
            database = self.database
            )
        self.cursor = self.db.cursor()
        
    def close(self):
        self.cursor.close()
        self.db.close()
        
