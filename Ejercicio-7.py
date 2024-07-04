"""
Ejercicio 7 - Bucle for

1.Darle al usuario un mensaje de
bienvenida al Cine La plata y pedirle el correo electrónico.

2.Verificar que el mail contenga un
único arroba. En caso que así sea indicarle acceso permitido y en caso
contrario volver a pedirle el correo.

3.Declarar una lista películas que
contenga “Rambo”
, “Nothing Hill” , “Patch
Adams “ y “Locademia de Policía”.

4.Pedirle al usuario que indique que
película desea ver.  Mediante un bucle for
verificar que la película se encuentre en cartelera. En caso que no sea así,
mostrarle las películas disponibles y pedirle que lo ingrese nuevamente.

5.Pedirle que ingrese la cantidad de
entradas que desea e informarle el costo total ($1000 por cada entrada
adquirida).

6.Informarle al usuario que va a
participar de un sorteo en el que tiene que adivinar el director de la película
ET. La cantidad de oportunidades que tiene para adivinarlo corresponderá a la
cantidad de entradas que adquirió.

7.En caso que adivine informarle que
tiene un descuento de un 50% y en caso contrario indicarle que perdió.

Estudiante Pablo Carrai
Correo pablo.carrai2024@fablab.mvl.edu.ar

"""
def ingresar():
    mail = input("Ingrese su correo electronico ")
    carrobas = 0
    for x in mail:
        if x == "@":
            carrobas += 1

    if carrobas != 1:
        print("Su mail debe tener un unico arroba ")
        ingresar()

peliculas = ["Rambo","Nothing Hill","Patch Adams","Locademia de Policia"]
print("Bienvenido al Cine La plata")
ingresar()
print("Acceso Permitido")

pelicula_elegida = input("Ingrese que pelicula desea ver ")
while pelicula_elegida not in peliculas:
    print("Elija una pelicula en cartelera  ")
    for x in peliculas:
        print(x)
    pelicula_elegida = input("Elija nuevamente ")

entradas_c = int(input("Ingrese la cantidad de entradas; cada una vale $1000   "))
print("Vas a participar de un sorteo, Adivina lo siguiente  ")
for x in range(entradas_c):
    adivinar = input("Quien dirigio ET?  ")
    if adivinar == "Steven Spielberg":        
        print("Adivinaste, te ganaste un descuento de $",((entradas_c * 1000) / 2))
        exit()
    else: 
        print("No es correcto  ")
print("Debes $",(entradas_c * 1000))
exit()