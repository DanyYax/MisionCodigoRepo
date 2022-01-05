
"""
Reto Mision Codigo Enero 2 2022

Dado un entero positivo debes encontrar la raíz cuadrada sin usar funciones 
incluidas como math.sqrt o el operador **
Tu función debe dar resultado con 3 decimales de exactitud.

@author: Dany Jacquez
"""

def sqrt(x):
    """ 
    Funcion que implementa el método iterativo para calcular raiz cuadrada 
    Babiloniano
    """
    # este algoritmo requiere iniciar "adivinando"
    # para simplificar la implementacion usaremos 2
    # mejorando el inicio el algoritmo va a llegar a la solución más rápido
    # pero para este caso esta bien 
    
    inicio = 2.000
    siguiente = (inicio + x / inicio ) / 2
    #print(siguiente)
    while (abs(inicio - siguiente) > 0.1):
        inicio = siguiente
        siguiente = (inicio + x / inicio ) / 2
        #print(siguiente)
    return float('%.3f'%siguiente)
         
def pruebas():
    print("Vamos a probar 10 diferentes numeros y ver si tu implementacion es correcta")
    probar_num(5, 2.236)
    probar_num(10, 3.162)
    probar_num(33, 5.745)
    probar_num(51, 7.141)
    probar_num(66, 8.124)
    probar_num(100, 10.000)
    probar_num(101, 10.050)
    probar_num(200, 14.142)
    probar_num(333, 18.248)
    probar_num(500, 22.361)
        
def probar_num(x, esperado):
    res = sqrt(x)
    print("  probando raiz de {}".format(x),end='')
    if res == esperado:
        print(" CORRECTO")
    else:
        print(" INCORRECTO ... Tu resultado es {} pero deberia de ser {}".format(res, esperado))
        
pruebas()