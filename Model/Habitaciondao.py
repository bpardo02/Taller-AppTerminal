import mysql.connector
import csv
from Class.habitacion import Habitacion

class HabitacionDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Odrapth1020",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()
    
    def datosCSV(self, archivo_csv):
        with open (archivo_csv, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                id_room = int(row[0])
                numero = int(row[1])
                cantidad_max = int(row[2])
                orientacion = str(row[3])

                habitacion = Habitacion(id_room,numero,cantidad_max,orientacion)
                self.addHabitacion(habitacion)

    def addHabitacion(self, Habitacion):
        query = "INSERT INTO habitacion (id_room, numero, cantidad_max, orientacion) VALUES (%s,%s,%s,%s)"
        valores = (Habitacion.ide, Habitacion.numero, Habitacion.cantidad, Habitacion.orientacion)
        self.cursor.execute(query,valores)
        self.connection.commit()

        

