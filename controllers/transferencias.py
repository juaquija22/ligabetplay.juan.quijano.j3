import utils.corefiles as cf
import utils.screencontrollers as sc

def transferir_jugador():
    sc.limpiar_pantalla()
    equipos = cf.readJson("equipos")

    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar()
        return

    print("=== Equipos Disponibles ===")
    for eid, equipo in equipos.items():
        print(f"ID: {eid} - {equipo.get('nombre', 'Sin Nombre')}")

    equipo_origen = input("ID del equipo de origen: ")
    equipo_destino = input("ID del equipo de destino: ")

    if equipo_origen == equipo_destino:
        print("El equipo de origen y destino no pueden ser el mismo.")
        sc.pausar()
        return

    if equipo_origen not in equipos or equipo_destino not in equipos:
        print("Alguno de los equipos no existe.")
        sc.pausar()
        return

    jugadores_origen = equipos[equipo_origen].get("jugadores", {})
    if not jugadores_origen:
        print("El equipo de origen no tiene jugadores.")
        sc.pausar()
        return

    print("\n=== Jugadores en el equipo de origen ===")
    for jid, jugador in jugadores_origen.items():
        print(f"ID: {jid} - {jugador.get('nombre', 'Sin Nombre')}")

    jugador_id = input("ID del jugador a transferir: ")

    if jugador_id not in jugadores_origen:
        print("El jugador no existe en el equipo de origen.")
        sc.pausar()
        return

    jugador = jugadores_origen.pop(jugador_id)
    equipos[equipo_destino].setdefault("jugadores", {})[jugador_id] = jugador

    cf.writeJson("equipos", equipos)
    print(f"\n Jugador '{jugador['nombre']}' transferido correctamente.")
    sc.pausar()