import os  
from stdiomask import getpass
from prettytable import PrettyTable


# Definición de variables globales y constantes
calificacionesTupla = ()
calificacionesLista = list(calificacionesTupla)
numCalifi = 0


# Definición de funciones
# Función para menú de opciones 
def menu():
    print("--------------- SISTEMA SAEW 2.0 -------------")
    print("\n\t\t- Módulo profesor -\n")
    print("-------------------Bienvenido ----------------\n")
    print("¿Qué acción desea realizar?: ")
    print('*  1) Ingresar calificaciones')
    print('*  2) Mostrar calificaciones')
    print('*  3) Mostrar calificaciones de mayor a menor')
    print('*  4) Detalle de las calificaciones')
    print('*  5) Mostrar detalle de las calificaciones por archivo')
    print('*  6) Salir del sistema')
    while True:
        try:
            tipoAccion = int(input("Ingrese la opción: "))
            if tipoAccion in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    return tipoAccion

# Función para agregar calificaciones 
def agregarCalificaciones(arreglo, n):
    for i in range(n):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación final del estudiante {i + 1} (0-20): "))
                if 0 <= calificacion <= 20:
                    arreglo.append(calificacion)
                    break
                else:
                    print("Calificación fuera de rango. Debe estar entre 0 y 20.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

# Función para mostrar calificaciones 
def mostrarCalificaciones(arreglo):
    arreglo.sort()
    print("Las calificaciones registradas son:")
    print(arreglo)

# Función para mostrar calificaciones de mayor a menor
def mostrarCalificacionesDesc(arreglo):
    arreglo.sort(reverse=True)
    print("Las calificaciones registradas de mayor a menor son:")
    print(arreglo)

# Función para guardar información 
def guardarArchivo(data):
    os.makedirs("BDD", exist_ok=True)
    with open("BDD/reporte.txt", 'w') as archivo:
        archivo.write('* Detalle de las calificaciones\n')
        archivo.write(f'{data}')
    print("Información almacenada exitosamente")

# Función para mostrar información 
def mostrarArchivo():
    try:
        with open("BDD/reporte.txt") as archivo:
            lineas = archivo.readlines()
            for l in lineas:
                print(l, end="")
    except FileNotFoundError:
        print("No se encontró el archivo de reporte. Asegúrese de generar el reporte primero.")

# Función para mostrar detalles de calificaciones 
def mostrarDetalle(arreglo, califi):
    contadorApro = 0
    contadorRecha = 0
    contadorSuspen = 0
    sumCalifi = 0
    for i in arreglo:
        sumCalifi += i

    for i in calificacionesLista:
        if 1 <= i <= 8:
            contadorRecha += 1
        if 9 <= i <= 13:
            contadorSuspen += 1
        if 14 <= i <= 20:
            contadorApro += 1

    promedio = round((sumCalifi / califi), 2)

    # Crear una instancia de PrettyTable
    tabla = PrettyTable()
    # Definir los encabezados de la tabla
    tabla.field_names = ["Total estudiantes", "Promedio", "Aprobados", "Suspensos", "Reprobados"]
    # Agregar filas de datos a la tabla
    tabla.add_row([califi, promedio, contadorApro, contadorSuspen, contadorRecha])
    print(tabla)
    guardarArchivo(tabla)

# Función principal main 
def main():
    password = getpass(prompt="Ingresa tu contraseña: ", mask='*')
    if password == "sistemas":
        os.system('clear')
        caso = menu()
        while caso != 6:
            if caso == 1:
                os.system('clear')
                numCalifi = int(input("Ingrese el número de estudiantes del curso: "))
                agregarCalificaciones(calificacionesLista, numCalifi)
                os.system('clear')
                caso = menu()
            elif caso == 2:
                os.system('clear')
                mostrarCalificaciones(calificacionesLista)
                caso = menu()
            elif caso == 3:
                os.system('clear')
                mostrarCalificacionesDesc(calificacionesLista)
                caso = menu()
            elif caso == 4:
                os.system('clear')
                mostrarDetalle(calificacionesLista, numCalifi)
                caso = menu()
            elif caso == 5:
                os.system('clear')
                mostrarArchivo()
                print()
                caso = menu()
        os.system('clear')
        print("Muchas gracias")

    else:
        print("Usuario no encontrado")


# Ejecutar la función main
main()
