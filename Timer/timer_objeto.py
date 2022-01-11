import time

class Timer():
    def __init__(self, nombre):
        self.nombre = nombre
        self.inicio = None
        self.fin = None
        self.total = 0
    
    def iniciar(self):
        if self.inicio is not None:
            print("Timer {} ya inicio".format(self.nombre))
            return
        self.inicio = int(time.time_ns() / 1000000)
        
    def terminar(self):
        if self.inicio is None:
            print("Timer {} no ha iniciado".format(self.nombre))
            return
        if self.fin is not None:
            print("Timer {} ya termino".format(self.nombre))
            return
        self.fin = int(time.time_ns() / 1000000)
        self.total = self.fin - self.inicio
        
    def resetear_cronometro(self):
        self.inicio = None
        self.fin = None
        
    def resumen(self):
        if self.inicio is None:
            print("Timer {} no ha iniciado".format(self.nombre))
            return
        if self.terminar is None:
            print("Timer {} no ha terminado".format(self.nombre))
            return
        # Imprimimos el tiempo al momento
        print("Tiempo de {}: {} ms".format(self.nombre, self.total))
        
##### LISTA ####
lista = []

for i in range(10000000):
    lista.append(i)

crono = Timer("suma")
crono.iniciar()

# Obtener la suma de los numeros en una lista
suma_lista = 0
for i in lista:
    suma_lista += i

crono.terminar()
print(suma_lista)
crono.resumen()