
#Doy la binevenida al jugador
print ("Bienvenido al Juego de Piedra Papel o Tijera")

#Librería escogida random.choice(sequence): Selecciona y devuelve un único elemento aleatorio de una lista o cadena
#las librerias se importa siempre al principio del script

import random

opciones = ["piedra", "papel", "tijera"]

# La computadora elige al azar
computadora = random.choice(opciones)

# el jugador escoje por teclado cual es su opción

jugador = input("Elige piedra, papel o tijera: ")

# La variable "f" es la que llama a la función en {}
print(f"la computadora eligió: {computadora}")

# Aquí empezaría la lógica del juego




    




