"""
1. Imprimir un mensaje que indique "Sistema de selección de deporte"
2. Le pida al usuario que indique su género
3. Le soliciteal usuario su edad
4. Le pida tu altura.
5. Si el usuario ingresó "hombre", "masculino" o "varón", le imprima un mensaje que diga: Hombre: True. Caso contrario que indique False.
6. Si el usuario es mayor de edad, que idique Mayor: True, si no False.
7. Si la altura ingresada es superios a los 1,8 metros, indicar Alto: True, caso contrario indicar False.
8. Si el usuario es varón indicar un mensaje que diga "Puede jugar rugby: True", si no False.
9. Si es mujer y es alta, indicar "puede jugar volley: True", caso contrario False.
10. Si es varón alto, imprimir "puede jugar basket: True, sino False.
11. Si es varón menor a 50 año indicar True en puede jugar fútbol, caso contrario indicar false.

Estudiante: Pablo Carrai
Correo : pablo.carrai2024@fablab.mvl.edu.ar
"""

print("Sistema de seleccion de deporte")
genero = input("Ingrese su genero  ")
edad = int(input("Ingrese su edad  "))
altura = float(input("Ingrese su altura   "))

print("Hombre: ", (genero == "hombre" or genero == "masculino" or genero == "varon"))
print("Mayor: ", (edad >= 18))
print("Alto: ", (altura > 1.8))
print("Puede jugar rugby: ", (genero == "varon"))
print("Puede jugar futbol: ", (edad < 50 and genero == "varon"))
print("Puede jugar volley: ", (genero == "mujer" and altura > 1.8))
exit()