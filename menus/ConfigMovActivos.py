import os
import requests
import re
from tabulate import tabulate
import json
import uuid
from datetime import datetime


def getActivosData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

def getPersonalData():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    return data

def getActivosID(id):
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return [peticion.json()] if peticion.ok else []

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


##   RETORNO ACTIVO ( ESTADO SIN ASIGNACION )   ##
def RetornarActivo():
    id = input(f"""
Ingrese el id del activo que desea retornar: """)
    data = getActivosID(id)
    if data:
        if data[0]["idEstado"] != "0":  # CONDICION: PARA RETORNAR DEBE ESTAR EN ESTADO "ASIGNADO" (" 1 ")
            while True:
                print(tabulate(data, headers="keys", tablefmt="rounded_grid"))    
                opcion = input(f"""
Esta seguro que desea retornar este Activo ( Eliminar asignaciones y poner en estado "No Asigando" )?
    1. Si
    2. Cancelar
                   
Seleccione una opcion: """)
    
                if opcion == "1":
                    agregarHistorial = dict()
                    IdQuienRealizaRetorno = input(f"""
Ingrese el id de la persona que hace el retorno: """)
                    if getPersonalId(IdQuienRealizaRetorno):
                        fecha = datetime.now().strftime('%Y-%m-%d')
                        agregarHistorial["NroId"] = str(uuid.uuid4().hex[:4])
                        agregarHistorial["Fecha"] = fecha
                        agregarHistorial["tipoMov"] = "1"
                        agregarHistorial["idRespMov"] = IdQuienRealizaRetorno
                        dictSolo = data[0]
                        listaDeHistorial = dictSolo["historialActivos"]
                        listaDeHistorial.append(agregarHistorial)
                        data[0]["idEstado"] = "0"
                        data[0]["asignaciones"] = []
                        requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                        print(f"""
Activo retornado correctamente.""")
                        input(f"""
Presione enter para continuar.""")
                        break
                    else:
                        print("ID no encontrado en la data de personal.")
                        input(f"""
Presione enter para continuar.""")
                else:
                    break
        else:
            print(f"""
EL ACTIVO YA SE ENCUENTRA EN ESTADO NO ASIGNADO """)
            input(f"""
Presione enter para continuar.""")
    else:
        print(f"""
El ID ingresado no existe.""")
        input(f"""
Presione enter para continuar.""")

##    DAR DE BAJA   ##
def DarBajaActivo():
    id = input(f"""
Ingrese el id del activo que desea dar de baja: """)
    data = getActivosID(id)
    if data:
        if not data[0]["asignaciones"]:  # CONDICIONES ESPECIALES: 5. NO SE PUEDE ELIMINAR UN ACTIVO QUE SE ENCUENTRE ASIGNADO A UNA PERSONA O ZONA DE CAMPUS.
            while True:
                print(tabulate(data, headers="keys", tablefmt="rounded_grid"))    
                opcion = input(f"""
Esta seguro que desea dar de baja este Activo?
    1. Si
    2. Cancelar
                   
Seleccione una opcion: """)
    
                if opcion == "1":
                    agregarHistorial = dict()
                    IdQuienRealizaDadoBaja = input(f"""
Ingrese el id de la persona que da de baja el activo: """)
                    if getPersonalId(IdQuienRealizaDadoBaja):
                        fecha = datetime.now().strftime('%Y-%m-%d')
                        agregarHistorial["NroId"] = str(uuid.uuid4().hex[:4])
                        agregarHistorial["Fecha"] = fecha
                        agregarHistorial["tipoMov"] = "2"
                        agregarHistorial["idRespMov"] = IdQuienRealizaDadoBaja
                        dictSolo = data[0]
                        listaDeHistorial = dictSolo["historialActivos"]
                        listaDeHistorial.append(agregarHistorial)
                        data[0]["idEstado"] = "2"
                        requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                        print(f"""
Activo dado de baja correctamente.""")
                        input(f"""
Presione enter para continuar.""")
                        break
                    else:
                        print("ID no encontrado en la data de personal.")
                        input(f"""
Presione enter para continuar.""")
                else:
                    break
        else:
            print(f"""
NO SE PUEDE ELIMINAR UN ACTIVO QUE SE ENCUENTRE ASIGNADO A UNA PERSONA O
ZONA DE CAMPUS.""")
            input(f"""
Presione enter para continuar.""")
    else:
        print(f"""
El ID ingresado no existe.""")
        input(f"""
Presione enter para continuar.""")

##   CAMBIAR ASIGNACION   ##
def CambiarAsignacion():
    id = input(f"""
Ingrese el id del activo que desea Reasignar: """)
    data = getActivosID(id)
    if data:
        if data[0]["asignaciones"]:
            ReAsignacion = dict()
            while True:
                try:
                    asignacion = data[0]["asignaciones"]
                    print(tabulate(asignacion, headers="keys", tablefmt="rounded_grid"))
                    
                    if not ReAsignacion.get("id"):
                        ReAsignacion["NroAsignacion"] = str(uuid.uuid4().hex[:4])

                    if not ReAsignacion.get("FechaAsignacion"):
                        fecha = datetime.now().strftime('%Y-%m-%d')
                        ReAsignacion["FechaAsignacion"] = fecha
                       
                        
                    
                    if not ReAsignacion.get("TipoAsignacion"):
                        TipoNumero = input(f"""
OPCIONES:
1. Persona
2. Zona
                                           
Seleccione una opcion: """)
                        if TipoNumero == "1":
                            ReAsignacion["TipoAsignacion"] = "Personal"
                        elif TipoNumero == "2":
                            ReAsignacion["TipoAsignacion"] = "Zona"
                        else:
                            raise Exception("Opcion no valida.")
                        
                    
                    if not ReAsignacion.get("AsignadoA"):
                        if ReAsignacion.get("TipoAsignacion") == "Personal":
                            idPersonal = input(f"""
Ingrese el id de la persona a la que desea asignar: """)
                            if getPersonalId(idPersonal):
                                ReAsignacion["AsignadoA"] = idPersonal
                                break
                            else:
                                raise Exception("Id no encontrado.")
                        if ReAsignacion.get("TipoAsignacion") == "Zona":
                            idPersonal = input(f"""
Ingrese el id de la zona a la que desea asignar: """)
                            if getZonaId(idPersonal):
                                ReAsignacion["AsignadoA"] = idPersonal
                                break
                            else:
                                raise Exception("Id no encontrado.")
                except Exception as error:
                    print(error)
            listaParaAgregar = [ReAsignacion]
            print(tabulate(listaParaAgregar, headers="keys", tablefmt="rounded_grid"))
            opcion = input(f"""
Esta seguro que desea Reasignar el activo?
    1. Si
    2. Cancelar
                   
Seleccione una opcion: """)
            if opcion == "1":
                agregarHistorial = dict()
                data[0]["asignaciones"] = listaParaAgregar
                IdQuienRealizaDadoBaja = input(f"""
Ingrese el id de la persona que realiza la Reasignacion: """)
                if getPersonalId(IdQuienRealizaDadoBaja):
                    agregarHistorial["NroId"] = str(uuid.uuid4().hex[:4])
                    agregarHistorial["Fecha"] = fecha
                    agregarHistorial["tipoMov"] = "4"
                    agregarHistorial["idRespMov"] = IdQuienRealizaDadoBaja
                    dictSolo = data[0]
                    listaDeHistorial = dictSolo["historialActivos"]
                    listaDeHistorial.append(agregarHistorial)
                    data[0]["idEstado"] = "1"
                    requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                    print(f"""
Activo Reasignado correctamente.""")
                    input(f"""
Presione enter para continuar.""")
                else:
                    print("ID no encontrado en la data de personal.")
                    input(f"""
Presione enter para continuar.""")

        else:
            print(f"""
SOLO PUEDE REASIGNAR ACTIVOS QUE YA ESTEN ASIGNADOS ( IDESTADO = 1 )""")
            input(f"""
Presione enter para continuar.""")
    else:
        print(f"""
ID ingresado no existente""")
        input(f"""
Presione enter para continuar.""")

##   ENVIAR A GARANTIA   ##
def EnviarAGarantia():
    id = input(f"""
Ingrese el id del activo que desea enviar a garantia: """)
    data = getActivosID(id)
    if data:
        if not data[0]["asignaciones"]:  # CONDICIONES ESPECIALES: 1. NO SE PUEDE ENVIAR A GARANTIA UN ACTIVO QUE SE ENCUENTRE ASIGNADO A UNA PERSONA O ZONA DE CAMPUS.
            while True:
                print(tabulate(data, headers="keys", tablefmt="rounded_grid"))    
                opcion = input(f"""
Esta seguro que desea enviar a garantia este Activo?
    1. Si
    2. Cancelar
                   
Seleccione una opcion: """)
    
                if opcion == "1":
                    agregarHistorial = dict()
                    IdQuienRealizaDadoBaja = input(f"""
Ingrese el id de la persona que envia el activo a garantia: """)
                    if getPersonalId(IdQuienRealizaDadoBaja):
                        fecha = datetime.now().strftime('%Y-%m-%d')
                        agregarHistorial["NroId"] = str(uuid.uuid4().hex[:4])
                        agregarHistorial["Fecha"] = fecha
                        agregarHistorial["tipoMov"] = "3"
                        agregarHistorial["idRespMov"] = IdQuienRealizaDadoBaja
                        dictSolo = data[0]
                        listaDeHistorial = dictSolo["historialActivos"]
                        listaDeHistorial.append(agregarHistorial)
                        data[0]["idEstado"] = "3"
                        requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                        print(f"""
Activo enviado a garantia correctamente.""")
                        input(f"""
Presione enter para continuar.""")
                        break
                    else:
                        print("ID no encontrado en la data de personal.")
                        input(f"""
Presione enter para continuar.""")
                else:
                    break
        else:
            print(f"""
NO SE ENVIAR A GARANTIA UN ACTIVO QUE SE ENCUENTRE ASIGNADO A UNA PERSONA O
ZONA DE CAMPUS.""")
            input(f"""
Presione enter para continuar.""")
    else:
        print(f"""
El ID ingresado no existe.""")
        input(f"""
Presione enter para continuar.""")



def menuMovActivos():
    while True:
        try:
            os.system("clear")
            print(f""" 
    __  ___                                                  
   /  |/  /__  ____  __  __                                  
  / /|_/ / _ \/ __ \/ / / /                                  
 / /  / /  __/ / / / /_/ /                                   
/_/  /_/\___/_/ /_/\__,_/                                    
    __  ___           _           _            __            
   /  |/  /___ _   __(_)___ ___  (_)__  ____  / /_____  _____
  / /|_/ / __ \ | / / / __ `__ \/ / _ \/ __ \/ __/ __ \/ ___/
 / /  / / /_/ / |/ / / / / / / / /  __/ / / / /_/ /_/ (__  ) 
/_/ _/_/\____/|___/_/_/ /_/ /_/_/\___/_/ /_/\__/\____/____/  
   / __ \___     /   | _____/ /_(_)   ______  _____          
  / / / / _ \   / /| |/ ___/ __/ / | / / __ \/ ___/          
 / /_/ /  __/  / ___ / /__/ /_/ /| |/ / /_/ (__  )           
/_____/\___/  /_/  |_\___/\__/_/ |___/\____/____/            
                                                             

1. RETORNO DE ACTIVO
2. DAR DE BAJA ACTIVO
3. CAMBIAR ASIGNACION DE ACTIVO
4. ENVIAR A GARANTIA ACTIVO
5. REGRESAR AL MENU PRINCIPAL""")
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                RetornarActivo()
            elif opcion == "2":
                DarBajaActivo()
            elif opcion == "3":
                CambiarAsignacion()
            elif opcion == "4":
                EnviarAGarantia()
            elif opcion == "5":
                break
            else:
                raise Exception("Opcion no valida")
            

        except Exception as error:
            print(error)