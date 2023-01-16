from string import Template
html_header = """
<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="mystyle.css">
    </head>
<body>
    <div class="column2">
    <div class="card">
"""



html_end = """    
    </div>
    </div>

</body>
</html>
"""
#ingles a español
stats_es = {'hp': 'HP',
            'attack': 'Ataque',
            'defense': 'Defensa',
            'special-attack': 'Ataque Especial',
            'special-defense': 'Defensa Especial',
            'speed': 'Velocidad'}

tipos_es = {'bug': 'Bicho',
            'dark': 'Siniestro',
            'dragon': 'Dragón',
            'electric': 'Eléctrico',
            'fairy': 'Hada',
            'fighting': 'Lucha',
            'fire': 'Fuego',
            'flying': 'Volador',
            'ghost': 'Fantasma',
            'grass': 'Planta',
            'ground':'Tierra',
            'ice': 'Hielo',
            'normal': 'Normal',
            'poison': 'Veneno',
            'psychic': 'Psíquico',
            'rock':'Roca',
            'steel':'Acero',
            'water':'Agua'
            }

especial_es = {'legendary': 'Legendario',
               'mythical': 'Mítico',
               'baby': 'Bebé'
               }


validador_de_pokemon = "Favor ingresar un nombre válido de un Pokemón: "

validación_de_opcion = "Favor ingresar una opción que sea válida: "

menu_de_opciones = f'''Bienvenido a la Applicación Pokemón
            ¿Qué información desea obtener?
            
            1. Mostrar Pokedex
            2. Exhibir cadena evolutiva completa 
            0. Salir de la App
            >'''

mensaje_de_salida = '''Gracias por usar nuestra Applicación Pokemón, ¡Hasta la próxima!'''


mostrar_pokemon = '''¡Ingresa el nombre de un Pokemón para ser exhibido en la Pokedex. 
“Nota: Si el pokémon tiene espacios reemplace por "-".
No coloque ningún tipo de signo de puntuación adicional.
Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime.”  '''

mostrar_pokemon_evo = '''¡Ingresa el nombre de un Pokemón para que su cadena de evoluciones sea exhibida en la Pokedex. 
“Nota: Si el pokémon tiene espacios reemplace por "-".
No coloque ningún tipo de signo de puntuación adicional.
Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime.”  '''
# En caso que queramos realizar cadena evolutiva 

tarjeta_de_evoluciones = Template('''<div class='column1')>
    <div class='card')>
    <h1>#$id $name</h1>
        <img src="$url" width="150" height="150">
    <div class="container">
        $evo_previa.title()
     <h1><b>Tipo</b></h3>
        $tipos
        $tipos_especial
    
    </div>
    </div>
    
    
    ''')


template_de_evolucion = Template('''
<h1>#$id $name</h1> 
<div class="row">
    $cards
</div>
''')


cuadrado_evolucion = Template('''
<h1>#$id $name</h1> 
<div class="row">
    $cards_1

<h1>#$id $name</h1> 
<div class="row">
    $cards_2

<h1>#$id $name</h1> 
<div class="row">
    $cards_3 
''')

caso_de_evolucion  = '''Ingrese el Nombre de un Pokemón para exhibir su cadena de evolución.
“Nota: Si el pokémon tiene espacios reemplace por "-".
No coloque ningún tipo de signo de puntuación adicional.
Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime.”
'''