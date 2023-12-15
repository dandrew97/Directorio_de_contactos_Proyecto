#Importación de la libreria que permite modificar directorios dentro del sistema operativo
import os

CARPETA = 'contactos/' # Variable que será una constante y almacenará la ruta de la carpeta contactos
EXTENSION = '.txt' #Extensión de archivos

def app():
    #Revisa si la carpeta existe o no 
    crear_directorio()

    #Muestra el menú de opciones 
    mostrar_menu()

    # Preguntar al usuario la acciona a realizar
    preguntar = True
    while preguntar:
        opcion = int(input('Selecciones una opción: \r\n'))

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Editar Contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver Contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar Contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar Contacto')
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo')

#Función para agregar un nuevo contacto 
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    #Crear el archivo con el nombre que da el usuario
    with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
        archivo.write('Nombre: ' + nombre_contacto + '\r\n')

#Función que muestra el menú de opciones
def mostrar_menu():
    print('Seleccione del menú lo que desees hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

# Función que permite crear la carpeta de contactos 
def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

app()