"""
Crear un programa que:
Le pida al usuario que ingrese su nombre.
Le de un mensaje de bienvenida concatenando su nombre al sistema de Garbarino.
Le pida al usuario que indique que opción desea: Comprar electrdomésticos, comprar música o ambos.
En caso que seleccione la primer opción, indicarle que puede comprar una heladera ($50000), un TV ($35000) o una licuadora ($5000). El usuario deberá ingresar que desea comprar y el sistema almacenar el monto gastado en memoria.
Si selecciona comprar música, indicarle que se poseen los discos de Queen($500), Muse ($300) o The Beatles ($450). El usuario deberá seleccionar el disco y el sistema almacenar esa información en memoria.
Si el usuario selecciona ambas, el sistema deberá mostrarle primero las opciones  de electrodomésticos y luego de música.
Luego el programa deberá indicarle cuál fue el costo total de la compra , darle un mensaje de despedida y cerrar su ejecución.

Estudiante: Pablo Carrai
Correo: pablo.carrai2024@fablab.mvl.edu.ar

"""
gastos = 0  

def saludar(usuario, mensaje="Bienvenido"):
    return(mensaje + " " + usuario + " " + "al sistema Garbarino")

def comprar_electrodomesticos():
    global gastos
    menu = """
    Contamos con los siguientes Electrodomesticos
    1) Heladera $50000
    2) TV $35000  
    3) Licuadora $5000
    4) Salir
    """
    print(menu)
    eleccion = int(input("Elija una opcion  "))
    if eleccion == 1:
        gastos = gastos + 50000
    elif eleccion == 2:
        gastos = gastos + 35000
    elif eleccion == 3:
        gastos = gastos + 5000
    else:
        print("Gracias por su compra")
    print(f"Llevamos un gasto total de ${gastos}")

def comprar_musica():
    global gastos
    menu = """
    Contamos con los siguientes discos
    1) Queen $500
    2) Muse $300 
    3) The Beatles $450
    4) salir
    """
    print(menu)
    eleccion = int(input("Elija una opcion  "))
    if eleccion == 1:
        gastos = gastos + 500
    elif eleccion == 2:
        gastos = gastos + 300
    elif eleccion == 3:
        gastos = gastos + 450
    else:
        print("Gracias por su compra")
    print(f"Llevamos un gasto total de ${gastos}")
    
def menu():
    menus = """
    Elija una opcion
    1) Comprar electrodomesticos
    2) Comprar musica
    3) Ambas
    4) Salir 
    """

    print(menus)
    eleccion = int(input("Elija su opcion (1, 2, 3, 4)  "))
    if eleccion == 1:
        comprar_electrodomesticos()
        menu()
    elif eleccion == 2:
        comprar_musica()
        menu()
    elif eleccion == 3:
        comprar_electrodomesticos()
        comprar_musica()
        menu()
    else: 
        print("Su consumo total fue $", gastos)
        print("Gracias por usar nuestro sistema   ")   
        exit()    

      
nombre = input("Ingrese su nombre ")
print(saludar(nombre))
menu()
