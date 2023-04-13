
def sumar(a: int, b: int) -> int:
    resultado = a + b
    # print(f"La suma de {a} y {b} es igual a {resultado}")
    imprimir(a)
    return resultado

def imprimir(t):
    print(t)
    

def leer_datos() -> list[int]:
    with open("DebuggingDemo/datos.csv", "r") as f:
        lineas = f.readlines()
    lista_sin_encabezado = lineas[1:]
    datos = []
    for num in lista_sin_encabezado:
        n = num.split(",")
        for each in n:
            datos.append(int(each))
    return datos

# nombre = "Python"
# edad = 10
costo = 100
impuesto = 16

datos = leer_datos()
print(datos)
print(sumar(datos[0], datos[1]))
print(sumar(4, 8))
print(sumar(4, 89))
print(sumar(4, 9))


# sumar(1, 3)
# print(sumar(costo, impuesto))
