bienvenida = "Bienvenido al Supermercado La Ilusion"
print(bienvenida)
nombre = input("Ingrese su Nombre  ")
apellido = input("Hola "+ nombre + " " + "Ingrese su Apellido  ")
verduleria = float(input(nombre + " " + apellido + " " + "Le pedimos que ingrese cuanto gasto en la Verduleria  $"))
carniceria = float(input(nombre + " " + apellido + " " + "Ahora necesitariamos saber cuanto gasto en su compra en la carniceria  $"))
otros = float(input(nombre + " " + apellido + " Ahora necesitariamos saber cuanto gasto en otros rubros  $"))
gastos_totales = verduleria + carniceria + otros 
print("Usted Gasto en total $" + " " ,gastos_totales)
descuento = gastos_totales - (gastos_totales * 0.10)
print("Le aplicamos un descuento de 10 % y te queda $" , descuento)
print("Gracias por usar nuestro sistema")
exit()