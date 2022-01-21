"""
El reto de esta semana es hacer una función que convierta un string a mayúsculas 
"""

def mayus(s):
    res = ''
    for letra in s:
        # obtenemos el indice en el codigo ASCII
        # referencia http://sticksandstones.kstrom.com/appen.html
        
        ind = ord(letra)
        if ind < 65:
            # caracter no soportado
            res += letra
        elif ind <= 90:
            # la letra ya es mayuscula
            res += letra
        elif 122 >= ind >= 97:
            # es una letra minuscula
            # para hacerla mayuscula le sumamos 32
            res += chr(ind - 32)
            
    return res

    
print(mayus('prueba'))
#PRUEBA
print(mayus("Otra con MAS palabras"))
#OTRA CON MAS PALABRAS