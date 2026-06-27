#Doy la bienvenida al jugador
print ("Bienvenido al Juego de Piedra Papel o Tijera")

#Librería escogida random.choice(sequence): Selecciona y devuelve un único elemento aleatorio de una lista o cadena
#las librerias se importa siempre al principio del script

import random
# Aqui usamos una Lista 

opciones = ["piedra", "papel", "tijera"]

# La computadora elige al azar
computadora = random.choice(opciones)

# el jugador escoje por teclado cual es su opción

jugador = input("Elige piedra, papel o tijera: ")

# La variable "f" es la que llama a la función que al principio se escogio.
print(f"la computadora eligió: {computadora}")

# Aquí empezaría la lógica del juego...
# Se usa if, elif, and como comparación lógica y or que permite elegir entre varias opciones y terminamos con else.
# Bucle de decisión o reglas del Juego 
if jugador == computadora:
    print("Empate")
elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel"):
    print("Gana Jugador")
else:
    print("Pierde Jugador")

    print ("Es el Fin del Juego")   

#Fin del Juego