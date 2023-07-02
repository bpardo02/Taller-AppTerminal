import mysql.connector
from Class.huesped import Huesped

class HuespedDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Odrapth1020",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()

    def addHuesped(self, Huesped):
        query = "INSERT INTO huesped (rut_huesped, nombre_huesped, responsabilidad) VALUES(%s,%s,%s)"
        valores = (Huesped.rut, Huesped.nombre, Huesped.responsabilidad)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print('Huesped añadido con exito...')

        

    def deleteHuesped(self, rut):
        query = "DELETE FROM huesped WHERE rut_huesped = %s"
        valores = (rut,)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print('Huesped eliminado...')

    def listHuesped(self):
        query = "SELECT * FROM huesped"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        huespedes = []
        
        for result in results:
            huesped = Huesped(result[0], result[1], result[2])
            huespedes.append(huesped)
        return huespedes

