import mysql.connector
from Class.encargado import Encargado

class EncargadoDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hotelduermebien",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()

    def addEncargado(self, Encargado):
        query = "INSERT INTO encargado_info (rut_encargado, name_encargado, pass_encargado) VALUES (%s,%s,%s)"
        valores = (Encargado.id, Encargado.name, Encargado.password)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print('Usuario creado con exito')

    def loginEncargado(self, name, password):
        query = "SELECT * FROM encargado_info WHERE name_encargado = %s AND pass_encargado = %s"
        valores = (name, password)
        self.cursor.execute(query,valores)
        result = self.cursor.fetchone()
        print(result)
        if result:
            encargado = Encargado(result[0], result[1], result[2])
            return encargado
        else:
            return None

    def listEncargado(self):
        query = "SELECT * FROM encargado_info"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        encargados = []

        for result in results:
            encargado = Encargado(result[0], result[1], result[2])
            encargados.append(encargado)
        return encargados
    
    def editEncargado(self, encargado):
        query = "UPDATE encargado_info SET name_encargado = %s, pass_encargado = %s WHERE rut_encargado = %s"
        valores = (encargado.name, encargado.password, encargado.id)
        self.cursor.execute(query,valores)
        self.connection.commit()

    def deleteEncargado(self, id):
        query = "DELETE FROM encargado_info WHERE rut_encargado = %s"
        valores = (id, )
        self.cursor.execute(query,valores)
        self.connection.commit()


