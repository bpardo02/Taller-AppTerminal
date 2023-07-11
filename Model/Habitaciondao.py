import mysql.connector
import csv
from Class.habitacion import Habitacion

class HabitacionDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hotelduermebien",
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

    def listHabitacion(self):
        query = "SELECT * FROM habitacion"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        habitaciones = []

        for result in results:
            habitacion = Habitacion(result[0], result[1], result[2], result[3])
            habitaciones.append(habitacion)
        return habitaciones



        


