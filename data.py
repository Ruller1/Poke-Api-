
from get_module import get_info
from html_stats import *
import poke_validation as Pkv
from show import show_pics
from random import choice
import obtenerStats as oS
import html_stats as hts
import cadena_evo as cE
import sys 
import os
import time
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


#__________________________VALIDACION_NOMBRE__________________________________
responss = str(input(f'{hts.menu_de_opciones}:'))
while responss != '0' and responss != '1' and responss != '2':
    responss = (input(f'{hts.menu_de_opciones}:'))

if responss == '1' :
    pokemon = Pkv.validate(input(hts.mostrar_pokemon +':\n' ))
elif responss == '2':
    cE.evolucion_de_pokemon()
else:
    print(hts.mensaje_de_salida)
    time.sleep(3)
    os.system(op_sys)
    exit()

   


#VARIABLES
api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
pkinfo = get_info(api_url)
pkspecie = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/')
pkname = pkinfo["name"].capitalize()
pkid = pkinfo["id"]
pkimgurl = pkinfo['sprites']['other']['official-artwork']['front_default']
pkstats = pkinfo['stats']
pktype = pkinfo['types']
evo_previa = pkspecie['evolves_from_species']
pesoPK = pkinfo['weight']
pesoPK = pesoPK/10
codigoCero = 'Codigo-Cero'




