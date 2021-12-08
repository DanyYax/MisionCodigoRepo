#
# Misión Código
# Fecha: Junio 8 2021
#
# Este es el codigo para explicar el video sobre variables y funciones
# todos los projectos y ejemplos de este canal son para python 3
#


def pedro(x,y):
    print(x + y)


print(" ---------- Misión Código ----------")
print("  ----- Variables y funciones -----")


print("\n\nEjemplos de Variables")
print("-------------------------\n")

caja = 0
print("Caja = " + str(caja) + " y es de tipo " + str(type(caja)))

caja = "perro" # puede ser con dobles o sencillas
print("Caja = " + caja + f" y es de tipo {type(caja)}")

caja = 3.1416
print("Caja = {} y es de tipo {}".format(caja, type(caja)))

caja = 1j
print(f"Caja = {caja} y es de tipo {type(caja)}")

caja = False
print(f"Caja = {caja} y es de tipo {type(caja)}")

print("-" * 25)




print("\n\nEjemplos de Funciones")
print("-" * 25)


print(f"Le hablamos a Pedro con 2 y 3")
pedro(2, 3)

print(f"Le hablamos a Pedro con 2 y 7")
pedro(2, 7)

# Funciona Igual con variables
a = 2.2
b = 3.14
print(f"Le hablamos a Pedro con {a} y {b}")
pedro(a, b)


print("\n\nOtras Funciones incluidas en python")

f1 = len("HOLA")
print(f1)

f2 = complex(2)
print(f2)

f3 = divmod(7,3)
print(f3)

f4 = abs(-5)
print(f4)


print("\n\n Funciones en la variable (objeto)")
Caja = "    sOy una vaRiablE de tipo string  " # notese que la variable tiene mayuscula

print(caja)
print(Caja)

CajaCap = Caja.capitalize()
print(CajaCap)
print(Caja.capitalize())

# Mas Funciones
print(Caja.find("r"))
print(Caja.find("R"))
print(Caja.find("wqe"))

print(Caja.upper())

print(Caja.strip())
print(f"{Caja.strip()}!")

print("\nPodemos tomar secciones de nuestro string")
print(Caja[4:7])
print(Caja[:15])
print(Caja[20:])


# la Mision del dia
# utilizando solamente estas variables. Es decir que no se vale usar otras, solo puedes manipular estas.
# escribe las siguientes 3 cosas
#
# 1. Misión Código
# 2. Programar Python es PODEROSO
# 3. Tengo una idea

p1 = "No tEnGo uNa"
p2 = "loco"
p3 = "Idea"
p4 = "Poder"
p5 = "Programar"
p6 = "Python"
p7 = "Misión"
p8 = 'código'

# Escribe aqui tu código

r1 = p7 + " " + p8.capitalize()
letra_o = p2[1:2]
poderoso = f"{p4}{letra_o}{p7[2:3]}{letra_o}"
r2 = f"{p5} {p6} {p4[3:4]}{p7[2:3]} {poderoso.upper()}"
t = p1.find("tEnGo")
tengo = p1[t:t+5]
una = p1[9:]
r3 = f"{tengo.capitalize()} {una.lower()} {p3.lower()}"

print("-" * 25)
print(f"Misión Código")
print(r1)
print(f"Programar Python es PODEROSO")
print(r2)
print(f"Tengo una idea")
print(r3)
print("-" * 25)
