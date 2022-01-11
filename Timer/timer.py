import time

##### LISTA ####
lista = []

for i in range(10000000):
    lista.append(i)


# Obtener el tiempo antes de nuestra accion
inicio = int(time.time_ns() / 1000000)

# Obtener la suma de los numeros en una lista
suma_lista = 0
for i in lista:
    suma_lista += i

# ontener el tiempo al terminar la accion
final = int(time.time_ns() / 1000000)

print(suma_lista)
print("Tiempo en sumar mi lista {} ms".format(final - inicio))