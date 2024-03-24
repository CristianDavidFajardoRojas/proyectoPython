import os
import requests
import re

def getActivosData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

def getNroItem(Nro):
    for val in getActivosData():
        if val.get("NroItem") == Nro:
            return [val]
        
def getCodTransac(cod):
    for val in getActivosData():
        if val.get("CodTransaccion") == cod:
            return [val]

##   AGREGAR NUEVO ACTIVO   ##
def postActivos():
    nuevoActivo = list()
    while True:
        try:

            if not nuevoActivo.get("NroItem"):
                Nro = input(f"""
Ingrese el numero de item: """)
                if re.match(r'^[0-9]+$', Nro) is not None:
                    Nro = int(Nro)
                    if getNroItem(Nro):
                        raise Exception("Numero de item ya existente.")
                    else:
                        nuevoActivo["NroItem"] = Nro
                else:
                    raise Exception ("Asegurese de escribir solo números.")
                

            if not nuevoActivo.get("CodTransaccion"):
                cod = input(f"""
Ingrese el codigo de transaccion: """)
                if re.match(r'^[0-9]+$', cod) is not None:
                    cod = int(cod)
                    if getCodTransac():
                        raise Exception("Codigo de transaccion ya existente.")
                    else:
                        nuevoActivo["CodTransaccion"] = cod
                else:
                    raise Exception ("Asegurese de escribir solo números.")
                

            if not nuevoActivo["NroSerial"]:
                NroSerial = input(f"""
Ingrese el nuemro de serial ( Si no tiene, presione solo enter ): """)
                if NroSerial == "":
                    nuevoActivo["NroSerial"] = "Sin serial "
                elif re.match(r'^[A-Z0-9\-_]+$', NroSerial) is not None:
                    nuevoActivo["NroSerial"] = NroSerial
                else:
                    raise Exception("Serial no valido, recuerde que las letras deben ser mayusculas.")
                
            #if not nuevoActivo["CodCampus"]:



                

        except Exception as error:
            print(error)

##   MENU DE ACTIVOS   ##
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