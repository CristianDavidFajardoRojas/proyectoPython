import os

import menus.ConfigActivos as MenActivos
import menus.ConfigPersonal as MenPersonal
import menus.ConfigZonas as MenZonas
import menus.ConfigAsignacionActivos as MenAsignacion
import menus.ConfigReportes as MenReportes
import menus.ConfigMovActivos as MenMovimientos

def menu():
    while True:
        try:
            os.system("clear")
            print(f"""
   _____ _      __                          _________    ______       
  / ___/(_)____/ /____  ____ ___  ____ _   / ____( _ )  / ____/       
  \__ \/ / ___/ __/ _ \/ __ `__ \/ __ `/  / / __/ __ \// /            
 ___/ / (__  ) /_/  __/ / / / / / /_/ /  / /_/ / /_/  < /___          
/____/_/____/\__/\___/_/ /_/ /_/\__,_/   \____/\____/\|____/          
   / __ \___     /  _/___ _   _____  ____  / /_____ ______(_)___      
  / / / / _ \    / // __ \ | / / _ \/ __ \/ __/ __ `/ ___/ / __ \     
 / /_/ /  __/  _/ // / / / |/ /  __/ / / / /_/ /_/ / /  / / /_/ /     
/_____/\___/  /___/_/ /_/|___/\___/_/ /_/\__/\__,_/_/  /_/\____/      
  / ____/___ _____ ___  ____  __  _______/ /___ _____  ____/ /____    
 / /   / __ `/ __ `__ \/ __ \/ / / / ___/ / __ `/ __ \/ __  / ___/    
/ /___/ /_/ / / / / / / /_/ / /_/ (__  ) / /_/ / / / / /_/ (__  )     
\____/\__,_/_/ /_/ /_/ .___/\__,_/____/_/\__,_/_/ /_/\__,_/____/      
                    /_/                                               

                                                                                
OPCIONES:              
    1. ACTIVOS
    2. PERSONAL 
    3. ZONAS
    4. ASIGNACION DE ACTIVOS
    5. REPORTES
    6. MOVIMIENTO DE ACTIVOS
    7. SALIR
              
              """)
        
            opcion = int(input(f"""
Seleccione una opcion: """))
            if opcion == 1:
                MenActivos.menuActivos()
            elif opcion == 2:
                MenPersonal.menuPersonal()
            elif opcion == 3:
                MenZonas.menuZonas()
            elif opcion == 4:
                MenAsignacion.menuAsignacionActivos()
            elif opcion == 5:
                MenReportes.menuReportes()
            elif opcion == 6:
                MenMovimientos.menuMovActivos()
            elif opcion == 7:
                print(f"""

Gracias, Vuelva pronto!""")
                break
            else:
                raise Exception("Seleccion no valida.")

        except Exception as error:
            print(error)        

menu()
    