
#
# Script de ejemplos para
# Curso Basico de Python - Clase 7: IF ELSE ELIF
# 
# No olvides sucribirte a mi canal de Youtube
# www.youtube.com/c/misioncodigo
#
# También puedes seguirme en instagram @dany_goku
#
#
# Ejemplo 1
#
hambre = input("Tienes hambre?")
if (hambre == "si"):
    print("Deberias comer algo")
    
print("Final")

#
# Ejemplo 2
#
like = input("Te esta gustando este video?")
if (like == "si"):
    print("Dale like")
else:
    print("Dale no me gusta")
    
print("Final")

#
# Ejemplo 3
#

comer = input("Que quieres comer?")
if(comer == "pizza"):
    print("Hablar a Dominos pizza")
elif(comer == "tacos"):
    print("Pedir unos tacos!")
elif(comer == "esnalada"):
    print("En serio ???")
else:
    print("No tengo esa opción, parece que moriras de hambre")