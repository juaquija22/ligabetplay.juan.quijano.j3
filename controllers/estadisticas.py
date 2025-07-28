import os
import sys
import utils.corefiles as cf
import utils.screencontrollers as sc

Equipos = []
Partidos = []

def programar_fecha():
    sc.limpiar_pantalla()
    data = cf.readJson("equipos")
    equipos = data.get("equipos", {})

    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar()
        return

    print("Equipos disponibles:")
    for id, equipo in equipos.items():
        print(f"ID: {id} - Nombre: {equipo.get('nombre', 'Sin nombre')}")

    local_id = input("ID del equipo local: ")
    visitante_id = input("ID del equipo visitante: ")

    if local_id == visitante_id:
        print("Un equipo no puede jugar contra sí mismo.")
        sc.pausar()
        return

    if local_id not in equipos or visitante_id not in equipos:
        print("Alguno de los equipos no está registrado.")
        sc.pausar()
        return

    fecha = input("Fecha del partido: ")

    nuevo_partido = {
        "fecha": fecha,
        "local": local_id,
        "visitante": visitante_id,
        "goles_local": None,
        "goles_visitante": None
    }

    datos = cf.readJson("partidos")
    datos.append(nuevo_partido)
    cf.writeJson("partidos", datos)

    print("Partido programado exitosamente.")
    sc.pausar()

def registrar_marcador():
    sc.limpiar_pantalla()
    datos = cf.readJson("partidos")
    equipos = cf.readJson("equipos").get("equipos", {})

    if not datos:
        print("No hay partidos programados.")
        sc.pausar()
        return

    for i, p in enumerate(datos):
        local = equipos.get(p['local'], {}).get('nombre', 'Desconocido')
        visitante = equipos.get(p['visitante'], {}).get('nombre', 'Desconocido')
        print(f"{i + 1}. {local} vs {visitante} - Fecha: {p['fecha']}")

    try:
        idx = int(input("Seleccione el número del partido: ")) - 1
        if idx < 0 or idx >= len(datos):
            raise ValueError
    except:
        print("Selección inválida.")
        sc.pausar()
        return

    try:
        goles_local = int(input("Goles del equipo local: "))
        goles_visitante = int(input("Goles del equipo visitante: "))
    except:
        print("Los goles deben ser números enteros.")
        sc.pausar()
        return

    datos[idx]['goles_local'] = goles_local
    datos[idx]['goles_visitante'] = goles_visitante

    cf.writeJson("partidos", datos)
    print("Marcador registrado correctamente.")
    sc.pausar()

def ver_estadisticas():
    sc.limpiar_pantalla()
    datos = cf.readJson("partidos")
    equipos = cf.readJson("equipos").get("equipos", {})

    if not datos:
        print("No hay partidos registrados.")
    else:
        print("Estadísticas de partidos:")
        for p in datos:
            local = equipos.get(p['local'], {}).get('nombre', 'Desconocido')
            visitante = equipos.get(p['visitante'], {}).get('nombre', 'Desconocido')
            marcador = f"{p.get('goles_local', '-')} - {p.get('goles_visitante', '-')}"
            print(f"{p['fecha']}: {local} vs {visitante} Resultado: {marcador}")
    sc.pausar()

def estadisticas_menu():
    while True:
        sc.limpiar_pantalla()
        print("=== MENÚ DE ESTADÍSTICAS ===")
        print("1. Programar Fecha de Partido")
        print("2. Registrar Marcador")
        print("3. Ver Estadísticas de Partidos")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            programar_fecha()
        elif opcion == "2":
            registrar_marcador()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            sc.pausar()
