import os
import requests
import re
from tabulate import tabulate
import json

def getZonasData():
    peticion = requests.get("http://154.38.171.54:5502/zonas")
    data = peticion.json()
    return data

def getZonasID(id):
    peticion = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
    return [peticion.json()] if peticion.ok else []

def getZonas(zona):
    for val in getZonasData():
        if val.get("nombreZona") == zona:
            return [val]

##   AREGAR NUEVA ZONA   ##
def postZona():
    nuevaZona = dict()
    while True:
        try:
  
            if not nuevaZona.get("id"):
                last = getZonasData()[-1]
                id = last.get("id")
                id = int(id)
                nuevaZona["id"] = f"{id + 1}"


            if not nuevaZona.get("nombreZona"):
                zona = input(f"""
Ingrese el nombre de la nueva zona: """)
                if re.match(r'^[A-Z][a-zA-Z]*(\s[A-Z][a-zA-Z]*)*$', zona) is not None:
                    if getZonas(zona):
                        raise Exception("Zona ya existente.")
                    else:
                        nuevaZona["nombreZona"] = zona
                else:
                    raise Exception("Recuerde que todas las palabras deben iniciar con mayusculas.")
            

            if not nuevaZona.get("totalCapacidad"):
                totalCapacidad = input(f"""
Ingrese la capacidad total: """)
                if re.match(r'^\d+$', totalCapacidad) is not None:
                    totalCapacidad = int(totalCapacidad)
                    nuevaZona["totalCapacidad"] = totalCapacidad
                else:
                    raise Exception("Ingrese solo una cantidad numerica.")
                
            zona_lista = [nuevaZona]
            print(tabulate(zona_lista, headers="keys", tablefmt="rounded_grid"))
            print(f"""
¿Esta seguro que desea agregar la nueva zona?
    1. Si
    2. Cancelar""")
            
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                requests.post("http://154.38.171.54:5502/zonas", data=json.dumps(nuevaZona, indent=4).encode("UTF-8"))
                print(f"""
Zona agregada correctamente.""")
                input(f"""
Presione enter para continuar.""")
                break
            elif opcion == "2":
                break
            else:
                raise Exception("Seleccion no valida.")
                
            
                

        except Exception as error:
            print(error)

##   EDITAR ZONA   ##
def editarZona():
    id = input(f"""
Ingrese el id de la zona que desea editar: """)
    data = getZonasID(id)
    if data:
        while True:
            try:
                print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                print(f"""
OPCIONES: """)
                for i, (val, asd) in enumerate(data[0].items()):
                    print(f"{i+1}. {val}")
                opcion = int(input(f"""
Seleccione una opcion: """))
                if opcion >= 1 or opcion <= 3: 
                    modificacion = list(data[0].keys())[opcion - 1]
                    if modificacion == "id":
                        raise Exception(f"La opcion {modificacion} no se puede modificar.")
                    nuevoValor = input(f"""
Ingrese el nuevo valor para {modificacion}: """)
                    if modificacion == "totalCapacidad":
                        data[0][modificacion] = int(nuevoValor)
                    else:
                        data[0][modificacion] = nuevoValor
                    break
                else:
                    raise Exception("Seleccion no valida.")
            except Exception as error:
                print(error)

        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
        opcion = input(f"""
¿Esta seguro que enviar la modificacion?
    1. Si
    2. Cancelar
                       
Seleccione una opcion: """)
        if opcion == "1":
            requests.put(f"http://154.38.171.54:5502/zonas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
            print(f"""
Zona modificada correctamente.""")
            input(f"""
Presione enter para continuar.""")
        else:
            print(f"""
Se cancelo la modificacion""")
            input(f"""
Presione enter para continuar.""")
        

    else:
        print(f"""
El ID ingresado no existe.""")
        input(f"""
Presione enter para continuar.""")

##   BORRAR ZONA   ##
def deleteZona():
    id = input(f"""
Ingrese el id de la zona que desea eliminar: """)
    data = getZonasID(id)
    if data:
        while True:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))    
            opcion = input(f"""
Esta seguro que desea eliminar esta zona?
    1. Si
    2. Cancelar
                   
Seleccione una opcion: """)
    
            if opcion == "1":
                peticion = requests.delete(f"http://154.38.171.54:5502/zonas/{id}")
                print(f"""
Zona eliminada correctamente.""")
                input(f"""
Presione enter para continuar.""")
                break
            else:
                break
    else:
        print(f"""
El ID ingresado no existe.""")
        input(f"""
Presione enter para continuar.""")

######################   FILTROS   ######################
def getZonaPorId(id):
    zona = list()
    for val in getZonasData():
        if val.get("id") == id:
            zona.append(val)
    return zona

def getZonaPorNombre(nombre):
    zona = list()
    for val in getZonasData():
        if val.get("nombreZona") == nombre:
            zona.append(val)
    return zona

def getZonaPorTotal(total):
    zona = list()
    for val in getZonasData():
        if val.get("totalCapacidad") == total:
            zona.append(val)
    return zona

##   BUSCAR ZONA   ##
def menuBuscarZona():
    while True:
        try:
            os.system("clear")
            print(f"""
    ____                                _____                        
   / __ )__  ________________ ______   /__  / ____  ____  ____ ______
  / __  / / / / ___/ ___/ __ `/ ___/     / / / __ \/ __ \/ __ `/ ___/
 / /_/ / /_/ (__  ) /__/ /_/ / /        / /_/ /_/ / / / / /_/ (__  ) 
/_____/\__,_/____/\___/\__,_/_/        /____|____/_/ /_/\__,_/____/  
                                                                     
                                                                            
OPCIONES:
    1. Buscar zona segun su id.
    2. Buscar zona segun su nombre.
    3. Buscar zona segun su capacidad total.
    4. Regresar. """)
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                id = input(f"""
Escriba el id: """)
                print(tabulate(getZonaPorId(id), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "2":
                nombre = input(f"""
Escriba el nombre: """)
                print(tabulate(getZonaPorNombre(nombre), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "3":
                total = int(input(f"""
Escriba la cantidad total: """))
                print(tabulate(getZonaPorTotal(total), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "4":
                break
            else:
                raise Exception("Opcion no valida.") 

        except Exception as error:
            print(error)

##   MENU ZONAS   ##
def menuZonas():
    while True:
        try:
            os.system("clear")
            print(f"""
    __  ___                    _____                        
   /  |/  /__  ____  __  __   /__  / ____  ____  ____ ______
  / /|_/ / _ \/ __ \/ / / /     / / / __ \/ __ \/ __ `/ ___/
 / /  / /  __/ / / / /_/ /     / /_/ /_/ / / / / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/     /____|____/_/ /_/\__,_/____/  

                                                                            
OPCIONES:
    1. AGREGAR
    2. EDITAR
    3. ELIMINAR
    4. BUSCAR
    5. REGRESAR AL MENU PRINCIPAL              """)
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                postZona()
            elif opcion == "2":
                editarZona()
            elif opcion == "3":
                deleteZona()
            elif opcion == "4":
                menuBuscarZona()
            elif opcion == "5":
                break
            else:
                raise Exception ("Opcion no valida.")
        
        except Exception as error:
            print(error)