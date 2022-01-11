#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:45:57 2021

@author: Profesor Yax para Mision Codigo
"""

from selenium import webdriver
import time
from instapy import InstaPy

#Vamos a iniciar el script

# lo primero que tenemos que hacer es hacer log in a mi cuenta de instagram

class IG_bot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False
        
        
    def login(self):
        
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile = webdriver.FirefoxProfile() 
        profile.set_preference("general.useragent.override", user_agent)
        driver = webdriver.Firefox(profile)
        driver.set_window_size(360,640)

        #driver = webdriver.Firefox()
        self.driver = driver
        driver.implicitly_wait(5)

        url = "https://www.instagram.com/"
        driver.get(url)
        
        time.sleep(3)
        
        # ya que tenemos la pagina tenemos que encontrar el lugar para el username 
        username = driver.find_element_by_css_selector("input[name='username']")
        username.clear()
        username.send_keys(self.username)
        
        # lo que sigue es hacer lo mismo pero para el password
        password = driver.find_element_by_css_selector("input[name='password']")
        password.clear()
        password.send_keys(self.password)
        
        login_boton = driver.find_element_by_xpath("//button[@type='submit']")
        login_boton.click()
        
        time.sleep(10)
        self.is_logged_in = True
        
        
    def buscar_hashtag(self, ht):
        pass
        
    
    def crear_post(self) -> bool:
        if not self.is_logged_in:
            print("ERROR: Necesitas hacer login primero ...")
            return False
        
    
def prueba():
    bot = IG_bot('profesoryax', 'TheHobbit2090')
    bot.login()
    
        

def probando_InstaPy():
    session = InstaPy(username='profesoryax', password='TheHobbit2090', headless_browser=True)
    session.login()
    
    # vamos a configurar un par de cosas 
    session.set_dont_like(["naked", "nsfw"])
    
    # Like posts based on hashtags and like 3 posts of its poster
    #session.set_user_interact(amount=5, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(['megaman', 'mariomaker2', 'speedrun', 'megamanx'], amount=10)
    
    # Follow user based on hashtags (without liking the image)
    #session.follow_by_tags(['megaman', 'mariomaker2', 'speedrun', 'megamanx'], amount=6)
    
    session.end()
    
    
prueba()