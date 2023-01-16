###################
from string import Template
import get_module as getM 
import html_stats as hts
import data as dT 
import get_evolve_previa as gep


#############
if dT.pkname == 'Type-null':
    html_body = f'''<h1>#{dT.pkid} {dT.codigoCero}</h1>
            <img src="{dT.pkimgurl}" width="150" height="150">
        <div class="container">'''
    html_body += f'''{dT.evo_previa}
    <h4>Peso: {dT.pesoPK} Kg</h4>        
        <h2>Estadísticas</h2>
            <table>
                <tr>'''
else:
    html_body = f'''<h1>#{dT.pkid} {dT.pkname}</h1>
            <img src="{dT.pkimgurl}" width="150" height="150">
        <div class="container">'''
    html_body += f'''{dT.evo_previa}
    <h4>Peso: {dT.pesoPK} Kg</h4>
        <h2>Estadísticas</h2>
            <table>
                <tr>'''

links_sin_repetir = []
lista_de_links = []
fuerte_contra = Template(f'<span class="label $tipo">$fuerte</span>')
def superEfectivo():
    global html_body
    for h in lista_de_links:
        links_tipo2 = getM.get_info(h)
        links_sin_repetir.append(links_tipo2['damage_relations']['double_damage_to'])
    ultimo = []
    for i in range(len(links_sin_repetir)): 
        for j in range(len(links_sin_repetir[i])):
            if links_sin_repetir[i][j]["name"] not in ultimo:
                ultimo.append(links_sin_repetir[i][j]["name"]) 

    ultimo_esp = []
    for i in ultimo:
        ultimo_esp.append(hts.tipos_es[i])
    ultimo_esp_ord = sorted(ultimo_esp)

    for i in range(len(ultimo)):
        html_body += (fuerte_contra.substitute(fuerte=ultimo_esp[i], tipo=ultimo[i]))+'\n'


debil_contra = Template(f'<span class="label $tipo">$debil</span>')
def debilContra():
    global html_body
    links_sin_repetir = []
    for h in lista_de_links:
        links_tipo2 = getM.get_info(h)
        links_sin_repetir.append(links_tipo2['damage_relations']['double_damage_from'])

    ultimo = []
    for i in range(len(links_sin_repetir)): 
        for j in range(len(links_sin_repetir[i])):
            if links_sin_repetir[i][j]["name"] not in ultimo:
                ultimo.append(links_sin_repetir[i][j]["name"]) 

    ultimo_esp = []
    for i in ultimo:
        ultimo_esp.append(hts.tipos_es[i])
        ultimo_esp_ord = sorted(ultimo_esp)
    for i in range(len(ultimo)):
        html_body += (debil_contra.substitute(debil=ultimo_esp[i], tipo=ultimo[i]))+'\n'



#
resistente_contra = Template(f'<span class="label $tipo">$resiste</span>')
def resistenteContra():
    global html_body    
    links_sin_repetir = []
    for h in lista_de_links:
        links_tipo2 = getM.get_info(h)
        links_sin_repetir.append(links_tipo2['damage_relations']['half_damage_from'])


    ultimo = []
    for i in range(len(links_sin_repetir)): 
        for j in range(len(links_sin_repetir[i])):
            if links_sin_repetir[i][j]["name"] not in ultimo:
                ultimo.append(links_sin_repetir[i][j]["name"]) 

    ultimo_esp = []
    for i in ultimo:
        ultimo_esp.append(hts.tipos_es[i])
    ultimo_esp_ord = sorted(ultimo_esp)
    for i in range(len(ultimo)):
        html_body += (resistente_contra.substitute(resiste=ultimo_esp[i], tipo=ultimo[i]))+'\n'


#
def pocoEficaz():
    global html_body
    links_sin_repetir = []
    for h in lista_de_links:
        links_tipo2 = getM.get_info(h)
        links_sin_repetir.append(links_tipo2['damage_relations']['half_damage_to'])

    ultimo = []
    for i in range(len(links_sin_repetir)): 
        for j in range(len(links_sin_repetir[i])):
            if links_sin_repetir[i][j]["name"] not in ultimo:
                ultimo.append(links_sin_repetir[i][j]["name"]) 

    ultimo_esp = []
    for i in ultimo:
        ultimo_esp.append(hts.tipos_es[i])
    ultimo_esp_ord = sorted(ultimo_esp)

    for i in range(len(ultimo)):
        html_body += (inmune_contra.substitute(inmune=ultimo_esp[i], tipo=ultimo[i]))+'\n'



#
inmune_contra = Template(f'<span class="label $tipo">$inmune</span>')
def inmuneContra():
    global html_body
    links_sin_repetir = []
    for h in lista_de_links:
        links_tipo2 = getM.get_info(h)
        links_sin_repetir.append(links_tipo2['damage_relations']['no_damage_from'])


    ultimo = []
    for i in range(len(links_sin_repetir)): 
        for j in range(len(links_sin_repetir[i])):
            if links_sin_repetir[i][j]["name"] not in ultimo:
                ultimo.append(links_sin_repetir[i][j]["name"]) 

    ultimo_esp = []
    for i in ultimo:
        ultimo_esp.append(hts.tipos_es[i])
    ultimo_esp_ord = sorted(ultimo_esp)

    for i in range(len(ultimo)):
        html_body += (inmune_contra.substitute(inmune=ultimo_esp[i], tipo=ultimo[i]))+'\n'

#
ineficaz_contra = Template(f'<span class="label $tipo">$ineficaz</span>')
def ineficazContra():
    global html_body
    links_sin_repetir = []
    for h in lista_de_links:
        links_tipo2 = getM.get_info(h)
        links_sin_repetir.append(links_tipo2['damage_relations']['no_damage_to'])


    ultimo = []
    for i in range(len(links_sin_repetir)): 
        for j in range(len(links_sin_repetir[i])):
            if links_sin_repetir[i][j]["name"] not in ultimo:
                ultimo.append(links_sin_repetir[i][j]["name"]) 

    ultimo_esp = []
    for i in ultimo:
        ultimo_esp.append(hts.tipos_es[i])
    ultimo_esp_ord = sorted(ultimo_esp)
    for i in range(len(ultimo)):
        html_body += (ineficaz_contra.substitute(ineficaz=ultimo_esp[i], tipo=ultimo[i]))+'\n'
    

#












