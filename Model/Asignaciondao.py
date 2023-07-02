import mysql.connector
from Class.asignacion import Asignacion

class AsignacionDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Odrapth1020",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()

    def addAsignacion(self , asignacion):
        query = "INSERT INTO asignacion (id_asignacion, id_room, rut_encargado, dia, hora) VALUES (%s,%s,%s,%s,%s)"
        valores = (asignacion.id_asignacion, asignacion.id_room, asignacion.rut_encargado, asignacion.dia, asignacion.hora)
        self.cursor.execute(query, valores)
        self.connection.commit()
        print("Asignacion creada con exito...")

    
