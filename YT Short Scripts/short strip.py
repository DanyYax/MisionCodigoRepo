
# Ejemplo de uso de funcion strip
# suscribete a mision codigo en YouTube para mas tips y tutoriales

s = "     5 espacios   !     "

print(s)
print("String tiene {} caracteres".format(len(s)))

s2 = s.strip()
print(s2)
print("String tiene {} caracteres".format(len(s2)))

# Para quitar los espacios del lado izquierdo
s3 = s.lstrip()
print(s3)
print("String tiene {} caracteres".format(len(s3)))

# tambien podemos quitar los del lado derecho
s3 = s.rstrip()
print(s3)
print("String tiene {} caracteres".format(len(s3)))
