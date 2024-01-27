#1) Hacer un programa que gestiones datos para una escuela.

#El programa tiene que ser capaz de:
#a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre, 
#Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las 
#notas, cantidad de faltas, cantidad de amonestaciones recibidas.
#b) Mostrar los datos de cada alumno
#c) Modificar los datos de los alumnos
#d) Agregar alumnos
#e) Expulsar alumnos


registro_alumnos = {}

alumno = {}

alumno["nombre"] = input("Ingrese el nombre del alumno: ")
alumno["apellido"] = input("Ingrese el apellido del alumno: ")
alumno["fecha_nacimiento"] = input("Ingrese la fecha de nacimiento del alumno en formato DD/MM/AAAA: ")
alumno["dni"] = input("Ingrese el DNI del alumno: ")
alumno["nombre_tutor"] = input("Ingrese el nombre del tutor del alumno: ")
alumno["notas"] = [3,5,6,6]
alumno["faltas"] = 2
alumno["amonestaciones"] = 1

registro_alumnos[alumno["dni"]] = alumno

dni = input("Ingrese el DNI del alumno: ")

if dni in registro_alumnos:
    alumno = registro_alumnos[dni]
    print("Nombre: ", alumno["nombre"])
    print("Apellido: ", alumno["apellido"])
    print("Fecha de nacimiento: ", alumno["fecha_nacimiento"])
    print("DNI: ", alumno["dni"])
    print("Nombre del tutor: ", alumno["nombre_tutor"])
    print("Notas: ", alumno["notas"])
    print("Cantidad de faltas: ", alumno["faltas"])
    print("Cantidad de amonestaciones recibidas: ", alumno["amonestaciones"])
else:
    print("No se encontró un alumno con ese DNI.")


dni = input("Ingrese el DNI del alumno: ")

if dni in registro_alumnos:
    alumno = registro_alumnos[dni]
    opcion = input("Ingrese la opción que desea modificar: nombre, apellido, fecha de nacimiento, nombre del tutor:")
    
    if opcion == "nombre":
        alumno["nombre"] = input("Ingrese el nuevo nombre del alumno: ")
    elif opcion == "apellido":
        alumno["apellido"] = input("Ingrese el nuevo apellido del alumno: ")
    elif opcion == "fecha de nacimiento":
        alumno["fecha_nacimiento"] = input("Ingrese la nueva fecha de nacimiento del alumno en formato DD/MM/AAAA: ")
    elif opcion == "nombre del tutor":
        alumno["nombre_tutor"] = input("Ingrese el nuevo nombre del tutor del alumno: ")
    else:
        print("Opción incorrecta.")
else:
    print("No se encontró un alumno con ese DNI.")


alumno = {}

alumno["nombre"] = input("Ingrese el nombre del alumno: ")
alumno["apellido"] = input("Ingrese el apellido del alumno: ")
alumno["fecha_nacimiento"] = input("Ingrese la fecha de nacimiento del alumno en formato DD/MM/AAAA: ")
alumno["dni"] = input("Ingrese el DNI del alumno: ")
alumno["nombre_tutor"] = input("Ingrese el nombre del tutor del alumno: ")
alumno["notas"] = []
alumno["faltas"] = 0
alumno["amonestaciones"] = 0

registro_alumnos[alumno["dni"]] = alumno


dni = input("Ingrese el DNI del alumno que desea expulsar: ")

if dni in registro_alumnos:
    del registro_alumnos[dni]
    print("Alumno expulsado correctamente.")
else:
    print("No se encontró un alumno con ese DNI.")
