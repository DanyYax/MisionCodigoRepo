
#
# Listas 
#

lista_vacia = []
print (lista_vacia)

lista1 = [1, 2, 3, 5, 90.2, "Texto", 3]
print (lista1)

print(lista1[0])
print(lista1[2])

# -------------
print(" Mi lista tiene {} elementos".format(len(lista1)))


# Mutables
cuenta = []
for i in range(10):
    cuenta.append(i)

print(cuenta)


# lista tiene 10 elementos del 0 al 9
cuenta.pop()
print(cuenta)


cuenta.pop(2)
print(cuenta)


cuenta.insert(2, 5)
print(cuenta)

# 
# otras caracteristicas
#
l3 = ["pedro", "pablo", "dino"]
print("Lista de Strings: {}".format(l3))


cuenta.extend(l3)
print(cuenta)


print("Vilma" in l3)


l4 = [l3, 5, [8.0, 9.9]]
print(l4)



l3.append("pedro")
print(l3)


print(l3.count("pedro"))
print(l3.count("Pedro"))
print(l3.count("Vilma"))


































