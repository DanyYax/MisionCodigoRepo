# Lista con valores 

lis = [10, -1, 0, 30, 30, 40, 100, -10, 0, 0]

# Como quitamos los valores repetidos
# Conservando el orden de los elementos de la lista

d = dict.fromkeys(lis)
print(d)

lis2 = list(d)
print(lis2)