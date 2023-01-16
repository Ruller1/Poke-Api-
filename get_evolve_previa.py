import data as dT



if dT.evo_previa == None:
    dT.evo_previa = '    '
else:
    dT.evo_previa = dT.evo_previa['name'].capitalize()

    dT.evo_previa = f'<h4>Evolucion Previa: {dT.evo_previa}</h4>'
    

with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]


if dT.pkspecie == 'Type-Null'.lower():
    dT.pkspecie = 'codigo-cero'.capitalize()





