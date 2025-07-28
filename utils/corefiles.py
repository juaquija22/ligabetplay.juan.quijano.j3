import json
import os
from config import DB_PATH

def readJson(nombre):
    ruta = os.path.join(DB_PATH, f"{nombre}.json")
    if not os.path.exists(ruta):
        return {}
    with open(ruta, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return {}

def writeJson(nombre, datos):
    ruta = os.path.join(DB_PATH, f"{nombre}.json")
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def updateJson(diccionario, claves):
    for clave in claves:
        ruta = os.path.join(DB_PATH, f"{clave}.json")
        os.makedirs(DB_PATH, exist_ok=True)

        datos = readJson(clave)
        if clave not in datos or not isinstance(datos[clave], dict):
            datos[clave] = {}

        datos[clave].update(diccionario)
        writeJson(clave, datos)
        return False
    return True

def deleteJson(ruta):
    datos = readJson(ruta[0])
    actual = datos
    for clave in ruta[1:-1]:
        if clave not in actual:
            return False
        actual = actual[clave]
    if ruta[-1] in actual:
        del actual[ruta[-1]]
        writeJson(ruta[0], datos)
        return True
    return False

def initializeJson(estructura):
    ruta = os.path.join(DB_PATH, "equipos.json")
    if not os.path.exists(ruta):
        writeJson("equipos", estructura)
    else:
        datos = readJson("equipos")
        for k, v in estructura.items():
            if k not in datos:
                datos[k] = v
        writeJson("equipos", datos)
