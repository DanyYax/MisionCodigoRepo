#!/usr/bin/env python3

import csv

# lo primero que necesitamos es nuestro CSV
# CSV: Comma Separated Values
# lo mas sencillo es tenerlo en el mismo
# lugar donde guardes este tu script

estudiantes = []
csv_f = open("Estudiantes.csv", "r")
lector = csv.reader(csv_f, delimiter=",")

# ahora podemos leer cada fila con un for
for fila in lector:
    #print(fila)
    estudiantes.append(fila)
    
# ahora que ya vimos que se leyo cada linea
# quitamos ese print y ponemos uno de la lista final
print(estudiantes)






























#import csv

# Primero necesitamos un csv
# Esta en el mismo lugar donde tengo este script
#estudiantes = []
#with open('Estudiantes.csv', newline='') as csvfile:
#    lector = csv.reader(csvfile, delimiter=',')
#    for fila in lector:
#        print(fila)
#        estudiantes.append(fila)
        
#print(estudiantes)