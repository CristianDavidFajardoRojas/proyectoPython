import os

def menuActivos():
    while True:
        os.system("clear")
        print(f"""
    __  ___                    ___        __  _                 
   /  |/  /__  ____  __  __   /   | _____/ /_(_)   ______  _____
  / /|_/ / _ \/ __ \/ / / /  / /| |/ ___/ __/ / | / / __ \/ ___/
 / /  / /  __/ / / / /_/ /  / ___ / /__/ /_/ /| |/ / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/  /_/  |_\___/\__/_/ |___/\____/____/  
                                                                

OPCIONES:
    1. AGREGAR
    2. EDITAR
    3. ELIMINAR
    4. BUSCAR
    5. REGRESAR AL MENU PRINCIPAL
              
""")