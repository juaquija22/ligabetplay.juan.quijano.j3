import json 
import utils.corefiles as cor
import utils. screencontrollers as sc
import utils. validatedata as vd
import utils.corefiles as cf
from config import DB_PATH
import random


def equipos():
    sc.limpiar_pantalla
    ideq = random.randint(1023, 9876)
    teamname = vd.validatetext('Nombre del Equipo :')
    fecha = vd.validateInt('ano de creacion del Equipo :')
    origen = vd.validatetext('pais de origen del Equipo :')
    id = vd.validateInt('id del equipo :')
    eq = {
        ideq:{
            "nombre":teamname,
            "fundacion":fecha,
            "pais":origen,
            "idliga":id
        }
    }
    sc.pausar_pantalla


    if not cf.updateJson(eq,["equipos"]):
            print("equipo agregado exitosamente ")
            sc.pausar_pantalla
    else:
        print("No se pudo agregar el equipo ")
        sc.pausar_pantalla
        
