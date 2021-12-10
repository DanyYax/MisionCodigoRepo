#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 20:34:43 2021

@author: Dany Jacquez
"""

# En este script lo que quiero es crear una imagen para un post de Instagram. 
# Vamos a usar una imagen de fondo y solo le agregaremos Texto

from PIL import Image, ImageFont, ImageDraw 
import csv
from os.path import isfile
from os import rename, remove
import glob
from instabot import Bot
import time


def crear_imagen(texto_escribir:str, nombre_in:str) -> bool:
    
    TEMPLATE = "CreacionImagenes/Template1.png"
    FONT = 'CreacionImagenes/LemonMilk.otf'
    
    nombre = nombre_in
    
    # primero vamos a revisar que la imagen no exista ya
    if isfile(nombre):
        print("ERROR: El Archivo {} ya existe".format(nombre))
        return False
    
    imagen = Image.open(TEMPLATE)
    # tama;o 1080 x 1080
    fuente = ImageFont.truetype(FONT, 60)
    
    imagen_editable = ImageDraw.Draw(imagen)
    
    # usar color picker para escoger color en RGB
    # de google
    imagen_editable.text((1080/4,1080/3), texto_escribir, (227, 225, 227), font=fuente)
    
    # Vamos a convertirla a jpeg
    im_rgb = imagen.convert('RGB')
    
    try:
        im_rgb.save(nombre)
    except IOError:
        print("ERROR: La Imagen no pudo ser creada")
        return False
    
    print("Imagen '{}' ha sido creada".format(nombre))
    return True
    
    
def leer_de_google_sheets():
    # Lo primero es hacer una spreadsheet en goggle Sheets
    # Obtener el link: 
    # https://docs.google.com/spreadsheets/d/1csVX3M0a2NnxqMs4fVMYQoZ0Wvvx0GXRsLA7qxsLi6c/edit?usp=sharing
    
    # activar API Google sheets api
    # https://developers.google.com/sheets/api/quickstart/python
    # https://developers.google.com/workspace/guides/create-project
    
    # crear credenciales
    # descargar JSON
    
    # Isntalar modulos
    #   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    # correr google_sheets_api_sample.pyy
    pass


def leer_de_csv() -> list:
    ''' Esta funcion lee el csv y nos regresa la siguiente frase disponible '''
    with open('CreacionImagenes/PostsInstagram.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for fila in spamreader:
            # cada fila tiene 4 columnas
            # 0: numero de post
            # 1: String con la frase
            # 2: "Si" dependiendo si la frase ha sido usada
            # 3: Pie de Pagina para post en IG
            
            if fila[2].upper() == "NO" or fila[2] == "":
                return fila
    
def marcar_post_hecho_csv(num:int) -> None:
    ''' Esta funcion va a marcar el numero de post como hecho
        Para eso vamos a leer cada linea y volverla a escribir solo
        vamos amodificar la del post que ya hicimos
    '''
    nuestro_csv = 'CreacionImagenes/PostsInstagram.csv'
      
    tmpFile = "tmp.csv"
    with open(nuestro_csv, "r") as file, open(tmpFile, "w") as outFile:
        lector = csv.reader(file, delimiter=',')
        escritor = csv.writer(outFile, delimiter=',')
        
        # ahora pasamos el encabezado o "header"
        header = next(lector)
        escritor.writerow(header)
        
        # y ahora cada fila
        for row in lector:
            # revisamos el numero de post
            # el numero y el texto, que son las primeras dos columnas no cambian
            # pero la columna 3  debe ser actualizada para el post que hicimos
            if row[0] == num:
                row[2] = "SI"
            
            # Y escribimos la fila
            escritor.writerow(row)
            
    rename(tmpFile, nuestro_csv)


def publicar_post(post, pie_post):
    ''' Esta funcion publica la imagen a Intagram
        para esto usaremos instabot
    '''
    # borrar cookie para que funcione el login
    cookie_del = glob.glob("config/*cookie.json")
    remove(cookie_del[0])

    bot = Bot()
    bot.login(username = 'profesoryax',
              password = 'TheHobbit2090')
    
    bot.upload_photo(post,
           caption = pie_post)
    

def hacer_nuevo_post() -> None:
    
    DIR_POSTS = "CreacionImagenes/Posts"
    
    print("----------------------------")
    print("Hora de hacer un nuevo POST")
    nuevo_post = leer_de_csv()
    if nuevo_post is None:
        print("ERROR: Ya no tienes posts que crear en tu csv")
        raise IOError()
    
    nueva_frase = nuevo_post[1]
    num_post = nuevo_post[0]
    caption= nuevo_post[3]
    imagen = "auto_post_{}.jpg".format(num_post)
    if crear_imagen(nueva_frase, imagen):
        # Como la imagen fue creada ahora necesitamos actualizar nuestro csv
        marcar_post_hecho_csv(num_post)
        publicar_post(imagen, caption)
        
        # mover imagen a folder de Posts
        # nota que el bot cambia el nombre de la imagen asi que hay que considerar eso
        nombre_nuevo = imagen + ".REMOVE_ME"
        rename(nombre_nuevo, DIR_POSTS + "/" + imagen)
    
    print("Post {} terminado".format(num_post))
    print("----------------------------")

def main():
    hacer_nuevo_post()


if __name__ == "__main__":
    intervalo_posts_hrs = 12
    print("Corriendo creador de posts de Instagram")
    print(" Este programa creara un post cada {} horas".format(intervalo_posts_hrs))
    while True:
        try:
            hacer_nuevo_post()
        except IOError:
            # terminamos
            break
        # vamos a hacer un post cada 12 horas
        intervalo_posts_seg = intervalo_posts_hrs * 60
        print("Esperare {} horas para hacer otro post".format(intervalo_posts_hrs))
        time.sleep(intervalo_posts_seg)
    print("-------------")