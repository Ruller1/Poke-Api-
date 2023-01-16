
from html_stats import *
import poke_validation as Pkv
from show import show_pics
from random import choice
import obtenerStats as oS
import data as dT
import get_species as gS

#################    




#_____________________________LINKS_PARA_TIPOS_________________________________


for i in range(len(dT.pktype)):
    if "url" in dT.pktype[i]["type"].keys():
        oS.lista_de_links.append(dT.pktype[i]["type"]["url"])

    
#___________________________________STATS_________________________________________

for st in dT.pkstats:
    state_name_esp = stats_es[st['stat']['name']]
    oS.html_body += f"<td><h5>{state_name_esp}: {st['base_stat']}<h/5></td>"
    #print(state_name_esp, st['base_stat'])

oS.html_body += '''</tr>
                </table>
                <h3><b>Tipo</b></h3> 
                    
            '''


#___________________________________TIPO___________________________________________


gS.species()

#____________________________DESCRIPCION_ALEATORIA________________________________
b = []
for i in range(len(dT.pkspecie['flavor_text_entries'])):
    if dT.pkspecie['flavor_text_entries'][i]['language']['name'] == 'es':
        a = dT.pkspecie['flavor_text_entries'][i]['flavor_text']
        b.append(a)
oS.html_body += f'<p>{choice(b)}</p>'




#___________________________SUPER EFECTIVO CONTRA____________________________________
oS.html_body += f'<h3>Super efectivo contra:</h3>'
oS.superEfectivo()
    


#_________________________________DEBIL CONTRA_______________________________________

oS.html_body += f'<h3>Débil contra: </h3>'
oS.debilContra()



#_____________________________RESISTENTE_CONTRA____________________________________
oS.html_body +=f'<h3>Resistente contra: </h3>'
oS.resistenteContra()

#______________________________POCO EFICAZ CONTRA____________________________________
oS.html_body +=f'<h3>Poco Eficaz contra: </h3>'
oS.pocoEficaz()



#______________________________INMUNE_CONTRA____________________________________
oS.html_body += f'<h3>Inmune contra: </h3>'
oS.inmuneContra()


#_______________________________INEFICAZ_CONTRA___________________________________
oS.html_body += f'<h3>Ineficaz contra: </h3>'
oS.ineficazContra()


#___________________________________PRINT_HTML______________________________________

final_html = html_header + oS.html_body + html_end







