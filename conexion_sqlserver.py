
#Conexion
"""
try:
    connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=LAPTOP-E61EMV6J\SQLEXPRESS;DATABASE=Hospital')
    print("Exitosa conexion")
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)
"""

import pyodbc
 
#CREACION DE FUNCIONES
def Select_Doctores():
    print("")
    print("=== Listado de Doctores =====")
    conex = pyodbc.connect('DRIVER={SQL Server}; SERVER=LAPTOP-E61EMV6J\SQLEXPRESS;DATABASE=Hospital')
    cursorDoctor = conex.cursor()
    cursorDoctor.execute("SELECT * FROM Doctor")
    listaDocs = cursorDoctor.fetchall()
    for doctor in listaDocs:
            print(doctor)


def Select_Hospital():
    print("")
    print("=== Listado de Hospitales =====")
    conex = pyodbc.connect('DRIVER={SQL Server}; SERVER=LAPTOP-E61EMV6J\SQLEXPRESS;DATABASE=Hospital')
    cursorHospital = conex.cursor()
    cursorHospital.execute("SELECT * FROM Hospital")
    listHosp = cursorHospital.fetchall()
    for hosp in listHosp:
        print(hosp)

def Select_Empleado():
    print("")
    print("=== Listado de Empleados =====")
    conex = pyodbc.connect('DRIVER={SQL Server}; SERVER=LAPTOP-E61EMV6J\SQLEXPRESS;DATABASE=Hospital')
    cursorEmpl = conex.cursor()
    cursorEmpl.execute("SELECT * FROM Emp")
    listEmple = cursorEmpl.fetchall()
    for emple in listEmple:
        print(emple)


def Select_Dpto():
    print("")
    print("=== Listado de Departamento =====")
    conex = pyodbc.connect('DRIVER={SQL Server}; SERVER=LAPTOP-E61EMV6J\SQLEXPRESS;DATABASE=Hospital')
    cursorDepto = conex.cursor()
    cursorDepto.execute("SELECT * FROM Dept")
    listDepto = cursorDepto.fetchall()
    for depto in listDepto:
        print(depto)



def Menu():
    print("")
    print("=== ¿QUE QUIERES VES? =====")
    print("---- Recuerda que solo tienes 2 consultas")
    print("")
    valor = input("Ingrese su respuesta: ")


    consultas = 0

    while consultas < 2:

        if valor == "Doctores" or valor == "doctores":
            Select_Doctores()
            valor_preg = input("¿Deseas hacer otra consulta? ")
            if valor_preg == "Si" or valor_preg == "si":
                valor = input("Ingrese su respuesta: ")
                consultas =+1
            else:
                break;
            
        elif valor == "Departamento" or valor == "departamento":
            Select_Dpto()
            valor_preg = input("¿Deseas hacer otra consulta? ")
            if valor_preg == "Si" or valor_preg == "si":
                valor = input("Ingrese su respuesta: ")
                consultas =+1
            else:
                break;
            
            
        elif valor == "Hospital" or valor == "hospital":
            Select_Hospital()
            valor_preg = input("¿Deseas hacer otra consulta? ")
            if valor_preg == "Si" or valor_preg == "si":
                valor = input("Ingrese su respuesta: ")
                consultas =+1
            else:
                break;
            
        elif valor == "Empleado" or valor == "empleado":
            Select_Empleado()
            valor_preg = input("¿Deseas hacer otra consulta? ")
            if valor_preg == "Si" or valor_preg == "si":
                valor = input("Ingrese su respuesta: ")
                consultas =+1
            else:
                break;
            
        else: 
            print("No existe resultado de tu peticion")
            print("---- Recuerda que solo tienes 1 consultas")
            print("")
            valor = input("Ingrese su respuesta: ")
            consultas =+1
Menu()

