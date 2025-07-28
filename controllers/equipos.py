import json
import utils.corefiles as cf
import utils.screencontrollers as sc
import utils.validatedata as vd
from config import DB_PATH
import random
import os

def equipos():
    sc.limpiar_pantalla()
    ideq = random.randint(1023, 9876)
    teamname = vd.validatetext('Nombre del Equipo :')
    fecha = vd.validateInt('año de creación del Equipo :')
    origen = vd.validatetext('país de origen del Equipo :')
    id = vd.validateInt('id de la liga del equipo :')

    eq = {
        ideq: {
            "nombre": teamname,
            "fundacion": fecha,
            "pais": origen,
            "idliga": id,
            "jugadores": []
        }
    }

    if not cf.updateJson(eq, ["equipos", "equipos"]):
        print("Equipo agregado exitosamente")
    else:
        print("No se pudo agregar el equipo")
    
    sc.pausar()

def listar_equipos():
    sc.limpiar_pantalla()
    ruta = os.path.join("data", "equipos.json")
    
    if not os.path.exists(ruta):
        print("No hay equipos registrados.")
        sc.pausar()
        return

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            equipos = datos.get("equipos", {})
    except:
        print("Error al leer el archivo de equipos.")
        sc.pausar()
        return

    if len(equipos) == 0:
        print("No hay equipos registrados.")
    else:
        print("Lista de equipos:")
        for i, (id_equipo, equipo) in enumerate(equipos.items(), 1):
            try:
                print(f"{i}. {equipo['nombre']} (ID: {id_equipo}) - Fundación: {equipo['fundacion']}, País: {equipo['pais']}, Liga: {equipo['idliga']}")
            except:
                print(f"{i}. Datos incompletos para el equipo con ID {id_equipo}")
