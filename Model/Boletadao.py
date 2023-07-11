import mysql.connector
from Class.boleta import Boleta

class BoletaDAO():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hotelduermebien",
            database="hoteldb"
        )
        self.cursor = self.connection.cursor()


    def addBoleta(self, Boleta):
        query = "INSERT INTO detalle_boleta (id_detalle, id_asignacion, valor_pagado, medio_pago, fecha , hora) VALUES (%s,%s,%s,%s,%s,%s)"
        valores = (Boleta.id_detalle, Boleta.id_asignacion, Boleta.valor, Boleta.medio, Boleta.fecha, Boleta.hora)
        self.cursor.execute(query,valores)
        self.connection.commit()
        print("Boleta generada con exito...")

    def deleteBoleta(self, id):
        pass