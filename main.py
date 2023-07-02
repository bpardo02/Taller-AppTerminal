from Model.Admindao import AdminDAO
from Model.Encargadodao import EncargadoDAO
from Model.Huespeddao import HuespedDAO
from Model.Habitaciondao import HabitacionDAO
from Model.Boletadao import BoletaDAO
from Model.Responsabledao import ResponsableDAO
from Model.Asignaciondao import AsignacionDAO

from Class.responsable import Responsable
from Class.admin import Admin
from Class.encargado import Encargado
from Class.huesped import Huesped
from Class.habitacion import Habitacion
from Class.boleta import Boleta
from Class.asignacion import Asignacion

import os
import datetime


#BUCLE PARA EVITAR CIERRE
while True:
    def main():
        print('HOTEL DUERME BIEN')
        print('1: Modulo Administrador')
        print('2: Modulo Encargado')
        opcion = input('Menu: Seleccione su modulo: ')


        #FUNCIONES DE CRUD ADMIN PARA ENCARGADOS
        def accionAdmin():
            ##########DIVIDER##########

            
            print('1: Añadir Encargado')
            print('2: Editar Encargado')
            print('3: Listar Encargados')
            print('4: Eliminar Encargado')
            opcionAdmin = input('Menu ingrese su acción: ')

            if opcionAdmin == '1':
                encdao = EncargadoDAO()

                nomEnc = input('Ingresar username de encargado: ')
                rutEnc = input('Ingresar Rut de Encargado:')
                passEnc = input('Asignar password a Encargado: ')
                enc = Encargado(rutEnc, nomEnc, passEnc)
                encdao.addEncargado(enc)
                return accionAdmin()

            if opcionAdmin =='2':

                editdao = EncargadoDAO()
                idprevio = input('Ingresa el rut del usuario para editar: ')
                newnomEnc = input('Ingresa nuevo Username: ')
                newpassEnc = input('Ingresa el cambio de password: ')
                

                newEnc = Encargado(idprevio, newnomEnc, newpassEnc)
                editdao.editEncargado(newEnc)

                print('Usuario actualizado con exito...')
                return accionAdmin()

            if opcionAdmin == '3':

                listdao = EncargadoDAO()
                encargados = listdao.listEncargado()
                print(listdao)
                print('Lista de Encargados: ')
                for encargado in encargados:
                    print(f'Username: {encargado.name}')
                    print(f'Rut: {encargado.id} \n ')
                return accionAdmin()


            if opcionAdmin =='4':
                deletedao = EncargadoDAO()

                delete = input('Seleccione Rut para borrar usuario: ')
                deletedao.deleteEncargado(delete)

                print('Usuario borrado con exito...')
                return accionAdmin()

        #FUNCION AUTORIZAR ADMIN
        def auth():
                admindao = AdminDAO()
                name = input('Indique nombre de usuario: ')
                password = input('Indique contraseña: ')

                admin = admindao.login(name,password)
                if admin:
                    print(f'Ingreso exitoso, bienvenido/a {name}')
                    return accionAdmin()
                else:
                    os.system('cls')
                    print('error autenticación, por favor reintente')
                    return auth()
                
        #FUNCION TAREAS DE ENCARRGADO
        def tareasEncargado():
             
            ###DIVIDER###

            print('Opciones: ')
            print('1: Modulo Huesped: ')
            print('2: Agregar CSV de habitaciones')
            print('3: Asignar cliente a habitacion')
            print('4: Asignar Responsable')
            print('5: Generar Boleta')
            print('6: Asignar responsable y registrar')
            opcionEnc = input('Seleccionar Modulo: ')
            if opcionEnc =='1':
                print('Opciones: ')
                print('1: Añadir Huesped al sistema ')
                print('2: Eliminar huesped ')
                

                opcionHuesped = input('Selecciona tu opcion: ')

                if opcionHuesped == '1':
                    
                    rut = input('Ingrese RUT del huesped: ')
                    nombre = input('Ingrese nombre de huesped: ')
                    responsabilidad = input('Es responsable? S/N: ')
                    
                    huesped = Huesped(rut,nombre, responsabilidad)
                    huespeddao = HuespedDAO()
                    huespeddao.addHuesped(huesped)

                    return tareasEncargado()

                if opcionHuesped =='2':

                    rutdelete = input('Ingresa RUT para borrar huesped: ')
                    deletehuesped = HuespedDAO()
                    deletehuesped.deleteHuesped(rutdelete)

                    return tareasEncargado()
                
            if opcionEnc =="2":
                try:
                    hoteldao = HabitacionDAO()
                    archivo_csv = "Model\habitaciones.csv"
                    hoteldao.datosCSV(archivo_csv)
                    print("Datos cargados desde CSV")
                    return tareasEncargado()
                except Exception as e:
                    print("Ocurrio un error ", str(e))
                    return tareasEncargado()
                
            if opcionEnc =="3":
                idasignacion = input('Asigne su ID: ')
                
                listhabitacionDAO = HabitacionDAO()
                habitaciones = listhabitacionDAO.listHabitacion()
                for habitacion in habitaciones:
                    print(f'ID: {habitacion.ide}')
                    print(f'Numero: {habitacion.numero}')
                    print(f'Cantidad Maxima: {habitacion.cantidad}')
                    print(f'Orientacion: {habitacion.orientacion} \n ')

                idroom = input('Seleccione ID de habitacion: ')
                rutencargado = input('Indique rut de persona que atiende: ')
                fecha_hoy = datetime.datetime.now()
                hora_uno = fecha_hoy.time()
                dia = fecha_hoy.date()

                asignDAO = AsignacionDAO()
                asignacion = Asignacion(idasignacion, idroom, rutencargado, dia, hora_uno)
                asignDAO.addAsignacion(asignacion)



                

            if opcionEnc =="4":
                ide_responsable = input('Asignar ID de asignacion previa: ')
                rutresponsable = input('Indique Rut de la lista de huespedes: ')

                responsable = Responsable(ide_responsable, rutresponsable)
                respdao = ResponsableDAO()

                respdao.asignResponsable(responsable)

            
            if opcionEnc =="5":
                id_boleta = input('Ingrese el id de la boleta: ')
                id_asignacion = input('Ingrese el id de la asignacion: ')
                cantidad = input('Indique cantidad total de clientes: ')
                valor = 20000 * cantidad
                medio = input('Ingrese medio de pago: ')
                actual_fecha = datetime.datetime.now()
                fecha = actual_fecha.date()
                hora = actual_fecha.time()

                newBoleta = Boleta(id_boleta,id_asignacion, valor, medio, fecha, hora)
                boletadao = BoletaDAO()

                boletadao.addBoleta(newBoleta)


                return tareasEncargado()
                
        #FUNCION AUTORIZAR ENCARGADO
        def authEncargado():
                encargadodao = EncargadoDAO()
                nomEncargado = input('Indique nombre de usuario: ')
                passEncargado = input('Indique contraseña: ')

                encargado = encargadodao.loginEncargado(nomEncargado,passEncargado)
                if encargado:
                    print(f'Ingreso exitoso, bienvenido/a {nomEncargado}')
                    return tareasEncargado()

                else:
                     os.system('cls')
                     print('Error autenticación, por favor reintente')
                     return authEncargado()
        

        #MODULOS DE USUARIO
        if opcion == '1':
            return auth()
        elif opcion =='2':
            return authEncargado()
      
    #INICIALIZADOR
    if __name__ == "__main__":
        main()
        


