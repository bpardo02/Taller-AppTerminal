import mysql.connector
from Class.admin import Admin



class AdminDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Odrapth1020",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()

    def addUser(self, Admin):
        query = "INSERT INTO admin_info (rut_admin, pass_admin, name_admin) VALUES (%s,%s,%s)"
        valores = (Admin.id, Admin.password, Admin.username)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print('Usuario creado con exito')

    def login(self, username, password):
        query = "SELECT * FROM admin_info WHERE name_admin=%s AND pass_admin = %s"
        valores= (username,password)
        self.cursor.execute(query, valores)
        result = self.cursor.fetchone()
        print(result)
        if result:
            admin = Admin(result[0], result[1], result[2])
            return admin
        else:
            return None



