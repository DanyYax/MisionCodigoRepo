
import math

print("Ejemplo de programa para calcular Area de un circulo")
print("usando el radio")
print("-" * 20)
# 1. Obtener el Radio del circulo
r_in = input("Cual es el radio de tu circulo? ")
r = float(r_in)

# 2. Obtener el area del circulo usando formula
area = math.pi * pow(r,2)

# 3. Imprimir el area del circulo
print("El Area de un circulo con radio = {} es {}".format(r, area))