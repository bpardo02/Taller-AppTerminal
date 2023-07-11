import mysql.connector
from Class.responsable import Responsable

class ResponsableDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hotelduermebien",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()

    def asignResponsable(self, responsable):
        query = "INSERT INTO log_huesped (id_asignacion, rut_huesped) VALUES (%s,%s)"
        valores = (responsable.id_asignacion, responsable.rut_huesped)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print("Responsable agregado...")

    def deleteResponsable(self, rut):
        query = "DELETE FROM log_huesped WHERE rut_huesped = %s"
        valores = (rut,)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print("Eliminado con exito...")

        
        
