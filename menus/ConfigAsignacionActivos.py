import os
import requests
import re
from tabulate import tabulate
import json
import uuid

def getActivosData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

def getActivosID(id):
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return [peticion.json()] if peticion.ok else []

def getPersonalData():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    return data

def getZonasData():
    peticion = requests.get("http://154.38.171.54:5502/zonas")
    data = peticion.json()
    return data


######################   VALIDACIONES   ######################
def getPersonalId(id):
    for val in getPersonalData():
        if val.get("id") == id:
            return [val]

def getZonaId(id):
    for val in getZonasData():
        if val.get("id") == id:
            return [val]



##   CREAR ASIGNACION ( DEBE ESTAR EN NO ASIGNADO ( ID ESATDO = 0 ) )   ##
def asignarActivo():
    id = input(f"""
Ingrese el id del activo que desea asignar: """)
    data = getActivosID(id)
    if data:
        if data[0]["idEstado"] == "0":
            data[0]["idEstado"] = "1"
            listaDeAsigVacia = data[0]["asignaciones"]
            diccionario = dict()
            while True:
                try:
                    if not diccionario.get("id"):
                        diccionario["NroAsignacion"] = str(uuid.uuid4().hex[:4])

                    if not diccionario.get("Fecha"):
                        fecha = input(f"""
Ingrese la fecha de asignacion ( YY-MM-DD ): """)
                        if re.match(r'^\d{4}-\d{2}-\d{2}$', fecha) is not None:
                            diccionario["Fecha"] = fecha
                        else:
                            raise Exception("Fecha no valida, formato YY-MM-DD.")



                    if not diccionario.get("tipoAsignacion"):
                        print(f"""
ASIGNACION: 
1. Persona
2. Zona""")
                        eleccion = input(f"""
Seleccione una opcion: """)
                        if eleccion == "1":
                            diccionario["tipoAsignacion"] = "Personal"
                        elif eleccion == "2":
                            diccionario["tipoAsignacion"] = "Zona"
                        else:
                            raise Exception("Opcion no valida.")



                    if not diccionario.get("AsignadoA"):
                        if diccionario.get("tipoAsignacion") == "Personal":
                            idPersonal = input(f"""
Ingrese el id de la persona a la que desea asignar: """)
                            if getPersonalId(idPersonal):
                                diccionario["AsignadoA"] = idPersonal
                                break
                            else:
                                raise Exception("Id no encontrado.")
                        if diccionario.get("tipoAsignacion") == "Zona":
                            idPersonal = input(f"""
Ingrese el id de la zona a la que desea asignar: """)
                            if getZonaId(idPersonal):
                                diccionario["AsignadoA"] = idPersonal
                                break
                            else:
                                raise Exception("Id no encontrado.")
      
                except Exception as error:
                    print(error)


            listaDeAsigVacia.append(diccionario)
            diccionarioID = data[0]
            idPersonal = diccionario.get("AsignadoA")
            if diccionario["tipoAsignacion"] == "Personal":
                asd = diccionario["AsignadoA"]
                personal = getPersonalId(asd)[0]
                Nombre = personal.get("Nombre")
            else:
                asd = diccionario["AsignadoA"]
                Zona = getZonaId(asd)[0]
                Nombre = Zona.get("nombreZona")

        
            opcion = input(f"""
¿Esta seguro que desea asignar {diccionarioID['Nombre']} a {Nombre}?
    1. Si
    2. Cancelar
                       
Seleccione una opcion: """)
            if opcion == "1":
                agregarHistorial = dict()
                IdQuienRealizaAsignacion = input(f"""
Ingrese el id de la persona que realiza la asignacion: """)
                if getPersonalId(IdQuienRealizaAsignacion):
                    agregarHistorial["NroId"] = str(uuid.uuid4().hex[:4])
                    agregarHistorial["Fecha"] = fecha
                    agregarHistorial["tipoMov"] = "1"
                    agregarHistorial["idRespMov"] = IdQuienRealizaAsignacion
                    dictSolo = data[0]
                    listaDeHistorial = dictSolo["historialActivos"]
                    listaDeHistorial.append(agregarHistorial)
                    requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                    print(f"""
Activo asignado correctamente.""")
                    input(f"""
Presione enter para continuar.""")
                else:
                    print("ID no encontrado en la data de personal.")
                    input(f"""
Presione enter para continuar.""")
            else:
                print(f"""
Se cancelo la modificacion""")
                input(f"""
Presione enter para continuar.""")
        
        else:
            print(f"""
SOLO PUEDE ASIGNAR ACTIVOS QUE NO ESTEN ASIGNADOS ( IDESTADO = 0 )""") 
            
    else:
        print(f"""
ID ingresado no existente""")
        input(f"""
Presione enter para continuar.""")

##   BUSCAR ASIGNACION   ##
def getDataAsiganciones():
    result = []
    for val in getActivosData():
        if val.get("asignaciones"):
            diccitionarioss = val['asignaciones'][0]
            diccitionarioss["ID Activo"] = val.get("id")
            diccitionarioss["Nombre del Activo"] = val.get("Nombre")
            result.append(diccitionarioss)
    return result
    
def getAsignacionPorId(id):
    for val in getDataAsiganciones():
        if val.get("NroAsignacion") == id:
            return [val]



def menuAsignacionActivos():
    while True:
        try:
            os.system("clear")
            print(f"""
    __  ___                                          
   /  |/  /__  ____  __  __                          
  / /|_/ / _ \/ __ \/ / / /                          
 / /  / /  __/ / / / /_/ /                           
/_/ _/_/\___/_/ /_/\__,_/                _           
   /   |  _____(_)___ _____  ____ ______(_)___   ____ 
  / /| | / ___/ / __ `/ __ \/ __ `/ ___/ / __ \/ __  |
 / ___ |(__  ) / /_/ / / / / /_/ / /__/ / /_/ / / / /
/_/  |_/____/_/\__, /_/ /_/\__,_/\___/_/\____/_/ /_/ 
    ____      /____/_        __  _                   
   / __ \___     /   | _____/ /_(_)   ______  _____  
  / / / / _ \   / /| |/ ___/ __/ / | / / __ \/ ___/  
 / /_/ /  __/  / ___ / /__/ /_/ /| |/ / /_/ (__  )   
/_____/\___/  /_/  |_\___/\__/_/ |___/\____/____/    
                                                     
OPCIONES:
    1. CREAR ASIGNACION
    2. BUSCAR ASIGNACION
    3. REGRESAR AL MENU PRINCIPAL""")
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                asignarActivo()
            elif opcion == "2":
                id = input(f"""
Escriba el Numero de la asignacion: """)
                print(tabulate(getAsignacionPorId(id), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "3":
                break
            else:
                raise Exception("Opcion no valida")



        except Exception as error:
            print(error)