#
# Ejemplo 1 de errores de principante
# Subscribete a Mision Codigo en YouTube
# https://www.youtube.com/c/misioncodigo?sub_confirmation=1
#

class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_completo = f"{nombre} {apellido}"
    
    def decir_hola(self) -> None:
        print(f"Hola, me llamo {self.nombre}")

    def decir_hola_formal(self) -> None:
        print(f"Buen Dia, mi nombre es {self.nombre_completo}")
        
# Codigo Principal
print("-----------")
print("Errores comunes Ejemplo 1")

yo = Persona("Dany", "Goku")
yo.decir_hola()
yo.decir_hola_formal()

print("-----------")