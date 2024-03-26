import os
import requests
import re
from tabulate import tabulate
import json

def getPersonalData():
    peticion = requests.get("http://154.38.171.54:5502/personas")
    data = peticion.json()
    return data

######################   VALIDACIONES   ######################
def getPersonalID(id):
    peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
    return [peticion.json()] if peticion.ok else []
    
def getNroCC(nroCC):
    for val in getPersonalData():
        if val.get("nroId (CC, Nit)") == nroCC:
            return [val]

def getEmail(email):
    for val in getPersonalData():
        if val.get("Email") == email:
            return[val]

######################   FILTROS   ######################
def getPersonalSegunNombre(nick):
    nombres = list()
    for val in getPersonalData():
        if val.get("Nombre") == nick:
            lista1 = val["Telefonos"]
            diccionario1 = lista1[0]
            moviiil = diccionario1["movil"]
            casaaa = diccionario1["casa"]
            nombres.append({
                "ID": val.get("id"),
                "Nombre": val.get("Nombre"),
                "CC o Nit": val.get("nroId (CC, Nit)"),
                "Email": val.get("Email"),
                "Telefono Movil": moviiil.get("num"),
                "Telefono Casa": casaaa.get("num")
            })
    return nombres

def getPersonalSegunEmail(email):
    emails = list()
    for val in getPersonalData():
        if val.get("Email") == email:
            lista1 = val["Telefonos"]
            diccionario1 = lista1[0]
            moviiil = diccionario1["movil"]
            casaaa = diccionario1["casa"]
            emails.append({
                "ID": val.get("id"),
                "Nombre": val.get("Nombre"),
                "CC o Nit": val.get("nroId (CC, Nit)"),
                "Email": val.get("Email"),
                "Telefono Movil": moviiil.get("num"),
                "Telefono Casa": casaaa.get("num")
            })
    return emails

def getPersonalSegunTelefono(tel):
    telefono = list()
    for val in getPersonalData():
        lista1 = val["Telefonos"]
        diccionario1 = lista1[0]
        moviiil = diccionario1["movil"]
        casaaa = diccionario1["casa"]
        if moviiil.get("num") == tel or casaaa.get("num") == tel:
            telefono.append({
                "ID": val.get("id"),
                "Nombre": val.get("Nombre"),
                "CC o Nit": val.get("nroId (CC, Nit)"),
                "Email": val.get("Email"),
                "Telefono Movil": moviiil.get("num"),
                "Telefono Casa": casaaa.get("num")
            })
    return telefono

##   AGREGAR NUEVA PERSONA   ##
def postPersonal():
    nuevaPersona = dict()
    while True:
        try:
            last = getPersonalData()[-1]
            id = last.get("id")
            id = int(id)

            if not nuevaPersona.get("id"):
                nuevaPersona["id"] = f"{id + 1}"


            if not nuevaPersona.get("nroId (CC, Nit)"):
                nroCC = input(f"""
Ingrese la CC o Nit: """)
                if re.match(r'^\d{10}$', nroCC) is not None:
                    if getNroCC(nroCC):
                        raise Exception("CC o Nit ya existente.")
                    else:
                        nuevaPersona["nroId (CC, Nit)"] = nroCC
                else:
                    raise Exception("Recuerde escribir solo 10 digitos numericos.")
                

            if not nuevaPersona.get("Nombre"):
                nombre = input(f"""
Ingrese el nombre de la persona: """)
                if re.match(r'\b[A-Z][a-zA-Z]*\b', nombre) is not None:
                    nuevaPersona["Nombre"] = nombre
                else:
                    raise Exception("Recuerde iniciar con mayusculas cada nombre.")
                

            if not nuevaPersona.get("Email"):
                email = input(f"""
Ingrese el correo electronico: """)
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None:
                    if getEmail(email):
                        raise Exception("Correo electronico ya existente.")
                    else:
                        nuevaPersona["Email"] = email
                else:
                    raise Exception("Correo electronico no valido.")
                

            if not nuevaPersona.get("Telefonos"):
                telMovil = input(f"""
Ingrese el telefono movil: """)
                telCasa = input(f"""
Ingrese el telefono hogar: """)
                listaASD = [{
                    "movil":{},
                    "casa":{}
                }]
                diccionarioASD = listaASD[0]
                if re.match(r'^\d{10}$', telMovil) is not None: 
                    diccionarioASD["movil"] = {
                        "id": f"{id + 1}",
                        "num": telMovil}
                else:
                    raise Exception("Telofono no valido, ingrese solo 10 digitos numericos.")
                if re.match(r'^\d{10}$', telCasa) is not None:
                    diccionarioASD["casa"] = {
                        "id": f"{id + 1}",
                        "num": telCasa}
                else:
                    raise Exception("Telofono no valido, ingrese solo 10 digitos numericos.")
                nuevaPersona["Telefonos"] = listaASD

            persona_lista = [nuevaPersona]
            print(tabulate(persona_lista, headers="keys", tablefmt="rounded_grid"))
            print(f"""
¿Esta seguro que desea agregar la nueva persona?
    1. Si
    2. Cancelar""")
            
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                requests.post("http://154.38.171.54:5502/personas", data=json.dumps(nuevaPersona, indent=4).encode("UTF-8"))
                print(f"""
Persona agregada correctamente.""")
                input(f"""
Presione enter para continuar.""")
                break
            elif opcion == "2":
                break
            else:
                raise Exception("Seleccion no valida.")

        except Exception as error:
            print (error)

def editarPersonal():
    id = input(f"""
Ingrese el id del activo que desea modificar: """)
    data = getPersonalID(id)
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
                if opcion >= 1 or opcion <= 5: 
                    modificacion = list(data[0].keys())[opcion - 1]
                    if modificacion == "id":
                        raise Exception(f"La opcion {modificacion} no se puede modificar.")
                    if modificacion == "Telefonos":
                        print(f"""
OPCIONES DE TELEFONO: 
1. Movil
2. Casa""")
                        seleccion = input(f"""
Seleccione una opcion: """)
                        if seleccion == "1" or seleccion == "2":
                            nuevoValor = input(f"""
Ingrese el nuevo valor para {modificacion}: """)
                            lista1 = data[0]["Telefonos"]
                            diccionario1 = lista1[0]
                            moviiil = diccionario1["movil"]
                            casaaa = diccionario1["casa"]
                            if seleccion == "1":
                                moviiil["num"] = nuevoValor
                            elif seleccion == "2":
                                casaaa["num"] = nuevoValor
                            break
                        else:
                            raise Exception("Seleecion no valida.")
                    else:
                        nuevoValor = input(f"""
Ingrese el nuevo valor para {modificacion}: """)
                        data[0][modificacion] = nuevoValor
                        break
                else:
                    raise Exception("Opcion no valida.")

            except Exception as error:
                print(error)
    
        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
        opcion = input(f"""
¿Esta seguro que enviar la modificacion?
    1. Si
    2. Cancelar
                       
Seleccione una opcion: """)
        if opcion == "1":
            requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
            print(f"""
Persona modificada correctamente.""")
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

##   ELIMINAR PERSONA   ##
def deletePersona():
    id = input(f"""
Ingrese el id de la persona que desea eliminar: """)
    data = getPersonalID(id)
    if data:
        while True:
            print(tabulate(data, headers="keys", tablefmt="rounded_grid"))    
            opcion = input(f"""
Esta seguro que desea eliminar esta persona?
    1. Si
    2. Cancelar
                   
Seleccione una opcion: """)
    
            if opcion == "1":
                peticion = requests.delete(f"http://154.38.171.54:5502/personas/{id}")
                print(f"""
Persona eliminada correctamente.""")
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

##   BUSCAR PERSONAL   ##
def menuBuscarPersonal():
    while True:
        try:
            os.system("cls")
            print(f"""
    ____                                ____                                   __
   / __ )__  ________________ ______   / __ \___  ______________  ____  ____ _/ /
  / __  / / / / ___/ ___/ __ `/ ___/  / /_/ / _ \/ ___/ ___/ __ \/ __ \/ __ `/ / 
 / /_/ / /_/ (__  ) /__/ /_/ / /     / ____/  __/ /  (__  ) /_/ / / / / /_/ / /  
/_____/\__,_/____/\___/\__,_/_/     /_/    \___/_/  /____/\____/_/ /_/\__,_/_/   
                                                                                                                                               
                                                                            
OPCIONES:
    1. Buscar personal segun su id.
    2. Buscar personal segun su nombre.
    3. Buscar personal segun su correo.
    4. Buscar personal segun su telefono.
    5. Regresar. """)
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                id = input(f"""
Escriba el id: """)
                print(tabulate(getPersonalID(id), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "2":
                nombre = input(f"""
Escriba el nombre: """)
                print(tabulate(getPersonalSegunNombre(nombre), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "3":
                email = input(f"""
Escriba el email: """)
                print(tabulate(getPersonalSegunEmail(email), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "4":
                telefono = input(f"""
Escriba el telefono: """)
                print(tabulate(getPersonalSegunTelefono(telefono), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "5":
                break
        except Exception as error:
            print(error)


##   MENU PERSOSONAL   ##
def menuPersonal():
    while True:
        try:
            os.system("cls")
            print(f"""
    __  ___                    ____                                   __
   /  |/  /__  ____  __  __   / __ \___  ______________  ____  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / _ \/ ___/ ___/ __ \/ __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/  __/ /  (__  ) /_/ / / / / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/    \___/_/  /____/\____/_/ /_/\__,_/_/   

OPCIONES:
    1. AGREGAR
    2. EDITAR
    3. ELIMINAR
    4. BUSCAR
    5. REGRESAR AL MENU PRINCIPAL""")
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                postPersonal()
            elif opcion == "2":
                editarPersonal()
            elif opcion == "3":
                deletePersona()            
            elif opcion == "4":
                menuBuscarPersonal()
            elif opcion == "5":
                break
            else:
                raise Exception ("Opcion no valida.")
        
        except Exception as error:
            print(error)

