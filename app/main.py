
from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar_pantalla
import controllers.equipos as eq
from config import DB_PATH


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
                     pausar_pantalla()
                       
                elif opcion == 2:
                       pass
                elif opcion == 3:
                       pass
                elif opcion == 4:
                       pass
                elif opcion == 5:
                       pass
                elif opcion == 6:
                       pass
                elif opcion == 0:
                       print ('\n Saliendo')
                       break
                else:
                       print ('\n Opcion no valida')
                       pausar_pantalla()



                
    