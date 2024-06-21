"""
Realizar con estas tres listas un programa que:
1. Imprimir el mensaje "Bienvenido al sistema de gestión online de la biblioteca Nacional".
2. Declarar una lista llamada infantiles que contenga los títulos Blancanieves, Los Tres Chanchitos y Cenicienta.
3. Declarar una segnda lista, nombrar la como novelas con los títulos Don Quijote, y La Novicia Revelde.
4. Por último, crear una lista policiales con Sherlok Holmes y Muerte en el Nilo.
5. Le pida al usuario que indique que tarea quiere realizar: Ver libros disponibles, eliminar libros, agregar, ver el stock de libros o sair del sistema.
6. En caso que la opción ingresada no sea correcta, pedirle nuevamente que ingrese una opción.
7. Si selecciona la opción ver libros, pedirle que ingrese la categoría que desea ver. Debe poder ingresar la opción ver todas. Imprimirle los títulos correspondientes a la categoría seleccionada.
8. Si ingresa una opción incorrecta, darle la opción que intente nuevamente.
9. Si el usuario selecciona eliminar libros, pedirle el título del libro a borrar. En caso que el libro exista, eliminarlo de la lista. En caso que no exista, informárselo y pedirle que ingrese otro título.
10. Si desea agregar un libro, pedirle la categoría y el título e ingresarlo. En caso que la categoría no exista, informárselo y darle la posibilidad que lo reingrese.
11. Si decide ver el stock, pedirle que ingrese el título e imprimirle cuántos ejemplares existen del mismo.
12. Todas las opciones, después de ejecutarse, deben llevar al menu inicial.

Estudiante: Pablo Carrai
Correo: pablo.carrai2024@fablab.mvl.edu.ar


Arreglar lo de hay stock, tiene que pedir que libro es y decir cuantos hay

"""
lista_infantiles = ["Blancanieves", "Los Tres Chanchitos", "Cenicienta"]
lista_novelas =  ["Don Quijote","La Novicia Revelde"]
lista_policiales = ["Sherlok Holmes", "Muerte en el Nilo"]

def agregar_libro():
    print("Ingrese la categoria del libro que quiere agregar    ")
    eleccion = input("Categoria  ")
    if eleccion not in ("Infantil", "Novela", "Policial"):
        print("Tiene que ser una categoria existente, vuelva a intetarlo   ")
        agregar_libro()
    elif eleccion == "Infantil":
        libro = input("Ingrese el titulo del libro   ")
        lista_infantiles.append(libro)
    elif eleccion == "Novela":
        libro = input("Ingrese el titulo del libro   ")
        lista_novelas.append(libro)
    elif eleccion == "Policial":
        libro = input("Ingrese el titulo del libro   ")
        lista_policiales.append(libro)
    menu()

def stock_libros():
    libro = input("De que libro quiere saber cuanto stock hay?  ")
    cantidad = 0
    if libro in lista_infantiles:
        cantidad = lista_infantiles.count(libro)
    elif libro in lista_novelas:
        cantidad = lista_novelas.count(libro)
    elif libro in lista_policiales:
        cantidad = lista_policiales.count(libro)
    else:
        print("Elije un libro en stock ")
    print(f"De tal {libro} tenemos {cantidad} en stock")
    menu()

def eliminar_libro():
    eleccion = input("Que libro quiere eliminar?    ")
    if eleccion in lista_infantiles:
        lista_infantiles.remove(eleccion)
        print("Registro eliminado ", eleccion)
        menu()
    elif eleccion in lista_novelas:
        lista_novelas.remove(eleccion)
        print("Registro eliminado ", eleccion)
        menu()
    elif eleccion in lista_policiales:
        print("Registro eliminado ", eleccion)
        lista_policiales.remove(eleccion)
        menu()
    else:
        print("Elija un libro existente    ")
        eliminar_libro()

def mostrar_categoria():
    menus = """
    Los generos disponibles son
    1) Infantiles
    2) Novelas
    3) Policiales
    4) Ver todas las categorias

    """
    print(menus)
    eleccion = int(input("Diganos que elije      "))
    if eleccion == 1:
        for x in lista_infantiles:
            print(x)
    elif eleccion == 2:
        for x in lista_novelas:
            print(x)
    elif eleccion == 3:
        for x in lista_policiales:
            print(x)
    elif eleccion == 4:
        for x in lista_infantiles:
            print(x)
        for x in lista_novelas:
            print(x)
        for x in lista_policiales:
            print(x)    
    menu()

def menu():
    menus = """
    Elija una opcion
    1) Ver libros disponibles
    2) Eliminar libros
    3) Agregar libros al catalogo
    4) Ver el stock de libros
    5) Salir del sistema.
    """
    print(menus)
    eleccion = int(input("Elija su opcion (1, 2, 3, 4 o 5)  "))
    if eleccion == 1:
        mostrar_categoria()
    elif eleccion == 2:
        eliminar_libro()
    elif eleccion == 3:
        agregar_libro()
    elif eleccion == 4:
        stock_libros()
    elif eleccion == 5:
        print("Gracias por utilizar el sistema    ")
        exit()
    else:
        menu()
    

print("Bienvenido al sistema de gestión online de la biblioteca Nacional")
menu()
exit()