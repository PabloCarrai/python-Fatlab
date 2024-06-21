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

numero_jugador_1 = int(input("Ingrese un numero entre 1 y 10    "))
while numero_jugador_1 not in range(1,11):
    numero_jugador_1 = int(input("Denuevo , Ingrese un numero entre 1 y 10    "))

print("Jugador 2 es su hora de adivinar que numero eligio su rival   ")
numero_jugador_2 = int(input("Adivine el numero    "))
cpifies = 2

while numero_jugador_1 != numero_jugador_2:
    cpifies -= 1
    print(f"Te quedan {cpifies} intentos")
    numero_jugador_2 = int(input("Adivine el numero    "))
    if cpifies == 0:
        print("Perdiste")
        break

if numero_jugador_1 == numero_jugador_2:     
    print("Adivinastes ")
    print("Tu puntaje es", cpifies, "Puntos")

exit()