
# Ejemplo #1
# Imprimir un texto 500 veces
#for i in range(500):
#    print("Hola Mundo Ireal")

# #############################################    
# Ejemplo #2
# Definir una lista contando del 1 al 50
nums = []
for x in range(50):
    nums.append(x + 1)
    
print(nums)

# Version Corta / Avanzada
#print([i + 1 for i in range(50)])

# #############################################
# Ejemplo #3
# Aplicar una accion a todos los elementos de una lista

def cent_a_far(cent):
    return (cent * 9 / 5 + 32)

far = []
for grado in nums:
    far.append(cent_a_far(grado))
    
print(far)

# #############################################
# Ejemplo #4
# Leer un archivo de texto

print("Letra de Enter Sandman")
letra = []
with open("enter_sandman.txt") as f:
    for linea in f:
        letra.append(linea)
        
        
print(letra)

# #############################################
# Reto
# Usar Ciclo for para imprimir lar tablas de multiplicar del 1 al 10
print("Tablas de Multiplicar")
for i in range(10):
    n = i + 1
    print("Tabla de Multiplicar del {}:".format(n))
    for j in range(10):
        m = j + 1
        print("   {} X {} = {}".format(n, m, n * m))

# #############################################