"""
Ejercicio 6 - Bucle while

Desarrollar un juego en Python que:

Le pida al jugador 1 que ingrese un número entre 1 y 10.
Si el número es incorrecto, pedirle que lo ingrese nuevamente hasta que lo haga correctamente.
Indicarle  al jugador 2 que tiene tres chances de adivinar el número del jugador 1 y pedirle que ingrese el número.
A cada intento que no adivina, indicarle que el número no es correcto e informarle cuantos intentos le quedan.
Si adivina, indicarle su puntaje (3 puntos si adivino en el primer intento, 2 si lo adivino en el segundo y 1 si lo adivino en el tercero).

Estudiante Pablo Carrai
Correo pablo.carrai2024@fablab.mvl.edu.ar

"""
jugador_numero1 = input("Jugador 1 Ingrese su nombre  ")
numero_jugador_1 = int(input(f"{jugador_numero1} Ingrese un numero entre 1 y 10    "))
while numero_jugador_1 not in range(1,11):
    numero_jugador_1 = int(input(f"{jugador_numero1} Denuevo , Ingrese un numero entre 1 y 10    "))

jugador_numero2 = input("Jugador 2 Ingrese su nombre  ")
print(f"{jugador_numero2} es su hora de adivinar que numero eligio su rival {jugador_numero1}")
numero_jugador_2 = int(input(f"{jugador_numero2} Adivine el numero    "))
cpifies = 2

while numero_jugador_1 != numero_jugador_2:
    cpifies -= 1
    print(f"Te quedan {cpifies+1} intentos")
    numero_jugador_2 = int(input("Adivine el numero    "))
    if cpifies == 0:
        print(f"Perdiste, el numero a adivinar era {numero_jugador_1}")
        break

if numero_jugador_1 == numero_jugador_2:     
    print(f"Adivinastes, el numero a adivinar era {numero_jugador_1} ")
    print("Tu puntaje es", cpifies+1, "Puntos")

exit()