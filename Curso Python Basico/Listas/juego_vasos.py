#
# Proyecto: Juego de Feria 1
#
# Pasos:
# Darle like al video. 
# Preparar nuestros datos y variables
# Presentar las 3 opciones 
# Capturar elección del jugador
# Decidir resultado
# Mostrar resultado y Terminar el Juego

from random import randrange

opciones = [0, 0, 0]
numero_random = randrange(0,3)

opciones[numero_random] = 1
#print(numero_random)
#print(opciones)

print("Bienvenido a la feria")
print("Vamos a jugar un pequeño juego")
print()
print("Uno de estos vasos tiene una pelota")
print("-------------------------")
print("|   1   |   2   |   3   |")
print("-------------------------")
print("¿Puedes adivinar en cual esta?")
print()


eleccion = input("¿En cual crees que esta? 1, 2 o 3?\n")
eleccion_int = int(eleccion)
#print(eleccion_int)

gano = False
if(opciones[eleccion_int -1] == 1):
    gano = True
    
#print(gano)
if gano:
    print("FELICIDADES GANASTE !!!")
else:
    print("lo siento, perdiste ...")