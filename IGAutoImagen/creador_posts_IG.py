#
# Script para video de Mision Codigo
#
# BOT para hacer imagenes y publicarlas a Instagram automaticamente
#

from PIL import Image, ImageFont, ImageDraw
import os
import csv
from instabot import Bot
import glob
import time
import shutil

def leer_de_csv() -> list:
    ''' Esta funcion lee el csv y nos regresa la siguiente frase disponible '''
    with open('CreacionImagenes/PostsInstagram.csv', newline='') as csvfile:
        lector = csv.reader(csvfile, delimiter=",")
        for fila in lector:
            # cada fila tiene 4 columnas
            # 0: numero de post
            # 1: String con la frase
            # 2: "Si" dependiendo si la frase ha sido usada
            # 3: Pie de Pagina para post en IG
            if fila[2] == "":
                return fila
        
        return None
    

def crear_imagen(texto_escribir:str, nombre_in:str) -> bool:
    print("Creando Imagen {}".format(nombre_in))

    TEMPLATE = "CreacionImagenes/Template1.png"
    FONT = 'CreacionImagenes/LemonMilk.otf'

    # Revisar que la imagen no exista
    if os.path.isfile(nombre_in):
        print("ERROR: El Archivo {} ya existe".format(nombre))
        return False
    
    imagen = Image.open(TEMPLATE)
    # tamaño de image 1080x1080
    fuente = ImageFont.truetype(FONT, 60)
    
    imagen_editable = ImageDraw.Draw(imagen)
    imagen_editable.text((1080/4, 1080/3), texto_escribir, (227, 225, 227), font=fuente)
    
    # convertir imagen a jpeg
    img_final = imagen.convert("RGB")
    
    try:
        img_final.save(nombre_in)
    except IOError:
        print("ERROR: La Imagen no pudo ser creada")
        return False
        
    return True


def publicar_post(foto, caption) -> None:
    ''' Esta funcion publica la imagen a Intagram
        para esto usaremos instabot
    '''
    
    try:
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
    except:
        pass
    
    print("Entrando a Cuenta de Instagram")
    bot = Bot()
    bot.login(username = "MisionCodigo",
              password = "temp1234")
    
    print("Publicando nuevo Post")
    bot.upload_photo(foto, caption=caption)
    
    return


def clean_up(archivo:str) -> None:
    
    DIR_POSTS = "CreacionImagenes/Posts"
    
    print("Haciendo limpieza de archivos")
    nuevo_nombre = archivo + ".REMOVE_ME"
    
    # copiarlo a una nueva carpeta
    # asume que la carpeta existe
    print("Copiando imagen final {}".format(nuevo_nombre))
    shutil.copy(nuevo_nombre, DIR_POSTS + "/" + archivo)
    
    # borrar el archivo original
    print("Borrando imagen temporal")
    os.remove(nuevo_nombre)
    
    return


def marcar_post_hecho(num:int) -> None:
    ''' Esta funcion va a marcar el numero de post como hecho
        Para eso vamos a leer cada linea y volverla a escribir solo
        vamos amodificar la del post que ya hicimos
    '''
    arch =  'CreacionImagenes/PostsInstagram.csv'
    tmp = "temp.csv"
    
    with open(arch, "r") as file, open(tmp, "w", newline="") as outf:
        lector = csv.reader(file, delimiter=",")
        escritor = csv.writer(outf, delimiter=",")
        
        header = next(lector)
        escritor.writerow(header)
        
        for fila in lector:
            if fila[0] == num:
                fila[2] = "SI"
            
            escritor.writerow(fila)
            
    shutil.copy(tmp, arch)
    os.remove(tmp)
        

def hacer_post():
    print("----------------------------")
    print("Hora de hacer un nuevo POST")
    nuevo_post = leer_de_csv()
    if nuevo_post is None:
        print("ERROR: Ya no tienes posts que crear en tu csv")
        raise IOError()

    nueva_frase = nuevo_post[1]
    num_post = nuevo_post[0]
    caption = nuevo_post[3]
    
    imagen = "auto_post_{}.jpg".format(num_post)
    
    if crear_imagen(nueva_frase, imagen):
        # La imagen se creo correctamente
        publicar_post(imagen, caption)
        clean_up(imagen)
        marcar_post_hecho(num_post)
        
    else:
        print("ERROR: La imagen no pudo ser creada :(")
        raise IOError()
 
    print("Post {} terminado".format(num_post))
    print("----------------------------")
    
    
if __name__ == "__main__":
    intervalo_en_hrs = 12
    print("Corriendo creador de posts de Instagram")
    print(" Este programa creara un post cada {} horas".format(intervalo_en_hrs))
    while True:
        try:
            hacer_post()
        except IOError:
            print("Hubo un error durante la creacion del post")
        
        intervalo_seg = intervalo_en_hrs * 60
        print("Esperare {} horas para hacer otro post".format(intervalo_en_hrs))
        time.sleep(intervalo_seg)
        
        
# Funciones de prueba
#crear_imagen("Prueba", "imagen.jpg")
#print(leer_de_csv())
#publicar_post("imagen.jpg", "Prueba de mi bot...")
#clean_up("imagen.jpg")
#marcar_post_hecho("2")
#hacer_post()
