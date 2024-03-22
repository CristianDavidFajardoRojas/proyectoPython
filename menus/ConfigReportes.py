import os

def menuReportes():
    while True:
        os.system("clear")
        print(f"""
    __  ___                    ___        __  _                 
   /  |/  /__  ____  __  __   /   | _____/ /_(_)   ______  _____
  / /|_/ / _ \/ __ \/ / / /  / /| |/ ___/ __/ / | / / __ \/ ___/
 / /  / /  __/ / / / /_/ /  / ___ / /__/ /_/ /| |/ / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/  /_/  |_\___/\__/_/ |___/\____/____/  
                                                                

OPCIONES:
1. LISTAR TODOS LOS ACTIVOS
2. LISTAR ACTIVOS POR CATEGORIA
3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
4. LISTAR ACTIVOS Y ASIGNACION
5. LISTAR HISTORIAL DE MOV. DE ACTIVO
6. REGRESAR AL MENU PRINCIPAL

""")