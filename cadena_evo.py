
from get_module import get_info
from html_stats import *
from poke_validation import *
from show import show_pics
from string import Template


def evolucion_de_pokemon():
    pokemon = validate(input(f'{hts.mostrar_pokemon_evo}\n')) 
    pkevo = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}')
    pkspecie = get_info(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/')


    cadena_evo = (get_info(pkevo['evolution_chain']['url']))


    
    evosEevee = ['eevee', 'vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
    evos_de_eevee = []
    if pokemon in evosEevee:
        evos_de_eevee.append(cadena_evo['chain']['species']['name'])
        for i in range(8):
            evos_de_eevee.append(cadena_evo['chain']['evolves_to'][i]['species']['name'])
        

        html_body = ""
        pokemon_evo = Template(f'''<h1>#$pkid $pkname</h1>
            <img src="$pkimgurl" width="150" height="150">
            <h3 class="left"><b>Tipo</b></h3>'''  )

    


        for j in evos_de_eevee:
            api_url = f'https://pokeapi.co/api/v2/pokemon/{j}'
            pkinfo = get_info(api_url)
            pkname = pkinfo["name"].capitalize()
            pkid = pkinfo["id"]
            pkimgurl = pkinfo['sprites']['other']['official-artwork']['front_default']
            pktype = pkinfo['types']
            html_body += pokemon_evo.substitute(pkid=pkid,pkname=pkname,pkimgurl=pkimgurl)
            if len(pktype) == 1:
                html_body += f"<span class='label left {pktype[0]['type']['name']}'>{tipos_es[pktype[0]['type']['name']].title()}</span>"
            else:
                html_body += f"<span class='label left {pktype[0]['type']['name']}'>{tipos_es[pktype[0]['type']['name']].title()}</span>"
                html_body += f"<span class='label left {pktype[1]['type']['name']}'>{tipos_es[pktype[1]['type']['name']].title()}</span>"

    
            final_html = html_header + html_body + html_end

        show_pics(final_html, pkname)


    else:
    
        evoluciona_de_otro = []
        poke_base = []
        es_segunda_evo =[]
        es_tercera_evo = []

        tiene_1_evo = []
        tiene_2_evo = []
        tiene_3_evo = []

        if cadena_evo['chain']['evolves_to'] == []:
        
            tiene_1_evo.append(pokemon)
        elif cadena_evo['chain']['evolves_to'][0]['evolves_to'] == []:
           
            tiene_2_evo.append(pokemon)

        elif cadena_evo['chain']['evolves_to'][0]['evolves_to'][0]['evolves_to'] == []:
          
            tiene_3_evo.append(pokemon)

            

        evoluciona_2 = [] 
        for i in tiene_2_evo:
            evoluciona_2.append(cadena_evo['chain']['species']['name'])
            evoluciona_2.append(cadena_evo['chain']['evolves_to'][0]['species']['name'])
            list(set(evoluciona_2))

        evoluciona_3 = []
        for i in tiene_3_evo:
            evoluciona_3.append(cadena_evo['chain']['species']['name'])
            evoluciona_3.append(cadena_evo['chain']['evolves_to'][0]['species']['name'])
            evoluciona_3.append(cadena_evo['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])
            list(set(evoluciona_3))

        total_pokes = tiene_1_evo + evoluciona_2 + evoluciona_3

        html_body = ""
        pokemon_evo = Template(f'''<h1>#$pkid $pkname</h1>
            <img src="$pkimgurl" width="150" height="150">
            <h3 class="left"><b>Tipo</b></h3>''' )

        


        for j in total_pokes:
            api_url = f'https://pokeapi.co/api/v2/pokemon/{j}'
            pkinfo = get_info(api_url)
            pkname = pkinfo["name"].capitalize()
            pkid = pkinfo["id"]
            pkimgurl = pkinfo['sprites']['other']['official-artwork']['front_default']
            pktype = pkinfo['types']
            html_body += pokemon_evo.substitute(pkid=pkid,pkname=pkname,pkimgurl=pkimgurl)
            if len(pktype) == 1:
                html_body += f"<span class='label left {pktype[0]['type']['name']}'>{tipos_es[pktype[0]['type']['name']].title()}</span>"
            else:
                html_body += f"<span class='label left {pktype[0]['type']['name']}'>{tipos_es[pktype[0]['type']['name']].title()}</span>"
                html_body += f"<span class='label left {pktype[1]['type']['name']}'>{tipos_es[pktype[1]['type']['name']].title()}</span>"

        
        final_html = html_header + html_body + html_end

        show_pics(final_html, pkname)
