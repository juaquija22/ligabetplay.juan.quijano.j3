import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.screencontrollers import limpiar_pantalla, pausar_pantalla
from controllers import equipos, jugadores, transferencias, estadisticas

def menu():
    while True:
        limpiar_pantalla()
        print("=== GESTOR DE TORNEOS ===")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Transferencia de jugador")
        print("6. Ver estadísticas")
        print("0. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            equipos.registrar_equipo()
        elif opcion == "2":
            equipos.listar_equipos()
        elif opcion == "3":
            jugadores.registrar_jugador()
        elif opcion == "4":
            jugadores.listar_jugadores()
        elif opcion == "5":
            transferencias.transferir_jugador()
        elif opcion == "6":
            estadisticas.mostrar_estadisticas()
        elif opcion == "0":
            print(" Saliendo del sistema.")
            break
        else:
            print(" Opción no válida.")

        pausar_pantalla()

if __name__ == "__main__":
    menu()
