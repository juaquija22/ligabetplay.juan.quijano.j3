
import os
import random
import json
import utils.corefiles as cf
import utils.screencontrollers as sc
import utils.validatedata as vd

def jugadores():
    sc.limpiar_pantalla()

    idjg = random.randint(1023, 9876)
    nombrejug = vd.validatetext("Nombre del jugador:")
    posicion = vd.validatetext("Posición del jugador:")
    dorsal = vd.validateInt("Número del dorsal:")
    idliga = vd.validateInt("ID del equipo al que pertenece:")

    nuevo_jugador = {
        idjg: {
            "nombre": nombrejug,
            "posicion": posicion,
            "dorsal": dorsal,
            "ideq": idliga
        }
    }

    if not cf.updateJson(nuevo_jugador, ["jugadores"]):
        print("Jugador agregado exitosamente a la base de datos.")

        equipos_data = cf.readJson("equipos")
        equipos_dict = equipos_data.get("equipos", {})
        id_equipo = None

        for clave, datos in equipos_dict.items():
            if isinstance(datos, dict) and datos.get("idliga") == idliga:
                id_equipo = clave
                break

        if id_equipo:
            if "jugadores" not in equipos_dict[id_equipo]:
                equipos_dict[id_equipo]["jugadores"] = []

            equipos_dict[id_equipo]["jugadores"].append(idjg)
            equipos_data["equipos"] = equipos_dict
            cf.writeJson("equipos", equipos_data)
        else:
            print(f"No se encontró el equipo con idliga {idliga} para vincular el jugador.")
    else:
        print("No se pudo agregar el jugador.")

    sc.pausar()

def listar_jugadores():
    sc.limpiar_pantalla()

    datos = cf.readJson("jugadores")
    jugadores = datos.get("jugadores", {})

    if not jugadores:
        print("No hay jugadores registrados.")
    else:
        print("Lista de jugadores:\n")
        for i, (id_jugador, jugador) in enumerate(jugadores.items(), 1):
            nombre = jugador.get("nombre", "Desconocido")
            posicion = jugador.get("posicion", "Desconocida")
            dorsal = jugador.get("dorsal", "Sin número")
            idequipo = jugador.get("ideq", "Sin equipo")

            print(f"{i}. {nombre} (ID: {id_jugador}) - Posición: {posicion}, Dorsal: {dorsal}, ID Equipo: {idequipo}")

    sc.pausar()
