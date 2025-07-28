"""
Autor: Juan Pablo Quijano
Fecha: 2025-07-27
Descripción: este proyecto consiste en una liga betplay donde se pueden hacer transferencias de jugadores crear jugadores crear equipos
"""



import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import controllers.equipos as eq
import controllers.jugadores as jg
import controllers.estadisticas as es
import controllers.transferencias as tran


def main_menu():
        limpiar_pantalla()
        print (' === GESTOR DE TORNEOS ===')
        print ('1. Registrar equipo')
        print('2. Listar equipos')
        print ('3. Registrar jugador')
        print('4. Listar jugadores')
        print('5. Transferencia de jugador (venta o préstamo)')
        print('6. Ver estadísticas')
        print('0. Salir')
        try:
            op=int(input("\n elige una opcion :"))
            if 1 <= op <= 6:
                return op
        except:
                pass
        return None




if __name__ == "__main__":
        while True:
                opcion = main_menu()
                if opcion == 1:
                     eq.equipos()
                     pausar()
                       
                elif opcion == 2:
                       eq.listar_equipos()
                       pausar()
                elif opcion == 3:
                       jg.jugadores()
                       pausar()
                elif opcion == 4:
                       jg.listar_jugadores()
                       pausar()
                elif opcion == 5:
                       tran.transferir_jugador()
                       
                elif opcion == 6:
                       es.estadisticas_menu()
                      
                elif opcion == 0:
                       print ('\n Saliendo')
                       break
                else:
                       print ('\n Opcion no valida')
                       pausar()



                
    