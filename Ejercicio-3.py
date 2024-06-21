"""
Crear un programa en python que:
1. De un mensaje de bienvenida que diga "Automotores Carlitos"
2. Le pida al usuario que ingrese el monto que desea gastar.
3. Si el monto es menor a 1000000 le debe indicar que no se tienen autos de ese valor y darle la posibilidad que lo ingrese nuevamente.
4. Le pida al usuario que ingrese la marca que está buscando. En caso que ingrese un valor distinto a Ford o Chevrolet informarle que no se trabaja con esa marca y pedirla que la ingrese nuevamente.
5. Le pida al usuario que indique la cantidad de puertas. Si el valor ingresado no está entre 3 y 5 informarle que los autos no tienen esa cantidad de puertas y pedirle que reingrese la cantidad de puertas.
6. En todos los casos anteriores, si el usuario ingresa un valor incorrecto por segunda vez, darle un mensaje de despedida y cerrar la ejecución del programa.
7. Una vez almacenada la información del monto disponible, la marca y la cantidad de puertas indicarle:
   7.1 Si el monto ingresado es mayor a 5000000, la marca es ford y las puertas son 3 indicarle que se posee la Ford Ranger.
   7.2 Si el monto ingresado es menor a 2000000, la marca es chevrolet y las puertas son 3 o 5 indicarle que tiene disponible el Chevrolet Corsa.
   7.3 Si ingresó Ford de 4 puertas y el valor es menor a 4000000 informarle que se cuenta con la Ford Eco Sport.
   Este pincha
   7.4 Si el monto ingresado es mayor a 3000000 y menor a 6000000 y la marca es es Chevrolet informarle que se tiene la Chevrolet Tracker.
   7.5 En cualquier otro caso decirle que no se poseen autos con esas características.
8. Darle al usuario un mensaje de despedida y cerrar la ejecución del programa.

Estudiante: Pablo Carrai
Correo : pablo.carrai2024@fablab.mvl.edu.ar

"""
despedida = "Adios"
print("Bienvenidos a Automotores Carlitos")
monto = int(input("Ingrese el monto que puede gastar    "))
if monto < 1000000:
    print("No se tienen autos de ese valor")
    monto = int(input("Vuelva a Ingresar el monto que puede gastar    "))
    if monto < 1000000:
      print(despedida)
else:
    marca = input("Ingrese una marca de coche ")
    if marca != "Ford" and marca != "Chevrolet":
       print("No contamos con esa marca")
       marca = input("Ingrese otra marca de coche ")
       if marca != "Ford" and marca != "Chevrolet":
          print(despedida)
    else:
       puertas = int(input("Ingrese la cantidad de puertas  "))
       if puertas < 3 or puertas > 5:
          print("No contamos con esa cantidad de puertas  ")
          puertas = int(input("Ingrese la cantidad de puertas  "))
          if puertas < 3 or puertas > 5:
             print(despedida)
       if monto > 5000000 and marca == "Ford" and puertas == 3:
         print("Usted posee la Ford Ranger")
       elif monto < 2000000 and marca == "Chevrolet" and (puertas == 3 or puertas == 5):
          print("Tiene disponible el Chevrolet Corsa.")
       elif marca == "Ford" and puertas == 4 and monto < 4000000:
          print("Cuenta con la Ford Eco Sport.")
       elif monto > 3000000 and monto < 6000000 and marca == "Chevrolet":
          print("Tiene la Chevrolet Tracker.")
       else:
          print("no se poseen autos con esas características")

#print(despedida)

exit()
     