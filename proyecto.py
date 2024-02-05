#Importación de la libreria que permite modificar directorios dentro del sistema operativo
import os

CARPETA = 'contactos/' # Variable que será una constante y almacenará la ruta de la carpeta contactos
EXTENSION = '.txt' #Extensión de archivos

#Clase Contactos
class Contacto:
    #Constructor
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

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
            editar_contacto()
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

#Función para editar un contacto existente 
def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #Revisar si el archivo con el nombre de contacto ingresado existe
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Editar los campos solicitados - Estas son variables que almacenan los datos que ingrese el usuario
            nombre_contacto = input('Agrega el nuevo nombre:\r\n')
            telefono_contacto = input('Agrega el nuevo número telefónico:\r\n')
            categoria_contacto = input('Agrega la nueva Categoría:\r\n')

            #Instanciar clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Renombrar el archivo
            # os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Escribir en el archivo 
            archivo.write('Nombre: ' + contacto.nombre + '\r')
            archivo.write('Telefono: ' + contacto.telefono + '\r')
            archivo.write('Categoria: ' + contacto.categoria + '\r')    

            # Mostrar mensaje de exito 
            print('\r\n Contacto editado correctamente \r\n')

    else:
        print('Este contacto no existe')

    # Reiniciar la app
    app()

#Función para agregar un nuevo contacto 
def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')
    
    # Revisar si el archivo ya existe antes de crearlo
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

    if not existe:
        #Crear el archivo con el nombre que da el usuario
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Resto de atributos 
            telefono_contacto = input('Agrega el número telefónico:\r\n')
            categoria_contacto = input('Categoría Contacto:\r\n')

            # instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo 
            archivo.write('Nombre: ' + contacto.nombre + '\r')
            archivo.write('Telefono: ' + contacto.telefono + '\r')
            archivo.write('Categoria: ' + contacto.categoria + '\r')
            

            #Mostrar un mensaje de éxito 
            print('\r\n Contacto creado correctamente \r\n')
        
    else:
        print('El contacto ya ha sido creado')
    
    # Reiniciar la app
    app()

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

#Función que retorna un valor para revisar si el contacto existe o no; esta funcion es usada en la línea 52
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
    
app()