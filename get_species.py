import data as dT
import obtenerStats as oS
import html_stats as hS


def species():

    n = len(dT.pktype)
    for tp in range(n):
        oS.html_body += f"<span class='label {dT.pktype[tp]['type']['name']}'>{hS.tipos_es[dT.pktype[tp]['type']['name']].title()}</span>"
    

    for tp in range(n):
        if(dT.pkspecie['is_baby'] == True):
            dT.pkspecie['is_baby'] = 'baby'
            oS.html_body += f"<span class='label normal'>{hS.especial_es[dT.pkspecie['is_baby']].title()}</span>" 
        elif(dT.pkspecie['is_legendary'] == True):
            dT.pkspecie['is_legendary'] = 'legendary' 
            oS.html_body += f"</span><span class='label normal'>{hS.especial_es[dT.pkspecie['is_legendary']].title()}</span>" 

        elif (dT.pkspecie['is_mythical'] == True):
            dT.pkspecie['is_mythical'] = 'mythical'
            oS.html_body += f"</span></span><span class='label normal'>{hS.especial_es[dT.pkspecie['is_mythical']].title()}</span>"       