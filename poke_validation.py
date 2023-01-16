with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]
import html_stats as hts

def validate(name, p_l = pokemon_lista, mensaje = hts.validación_de_opcion):
    if name =='codigo-cero':
        name = 'type-null'
    while name not in p_l:
        name = input(mensaje).lower()

    return name

if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))
