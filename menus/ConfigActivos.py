import os
import requests
import re
from tabulate import tabulate
import json

def getActivosData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

def getMarcasData():
    peticion = requests.get("http://154.38.171.54:5502/marcas")
    data = peticion.json()
    return data

def getCategoriaData():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    return data

def getTipoData():
    peticion = requests.get("http://154.38.171.54:5502/tipoActivos")
    data = peticion.json()
    return data

def getActivosID(id):
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return [peticion.json()] if peticion.ok else []

######################   VALIDACIONES   ######################
def getNroSerial(Nro):
    for val in getActivosData():
        if val.get("NroSerial") == Nro:
            return [val]
        
def getCodTransac(cod):
    for val in getActivosData():
        if val.get("CodTransaccion") == cod:
            return [val]

def getCodCampus(cod):
    for val in getActivosData():
        if val.get("CodCampus") == cod:
            return [val]

def getNroFormu(Nro):
    for val in getActivosData():
        if val.get("NroFormulario") == Nro:
            return [val]

##   AGREGAR NUEVO ACTIVO   ##
def postActivos():
    nuevoActivo = dict()
    while True:
        try:

            if not nuevoActivo.get("NroItem"):
                last = getActivosData()[-1]
                NroItem = last.get("NroItem")
                asd = int(NroItem)
                nuevoActivo["NroItem"] = asd + 1
                

            if not nuevoActivo.get("CodTransaccion"):
                nuevoActivo["CodTransaccion"] = 327
             

            if not nuevoActivo.get("NroSerial"):
                NroSerial = input(f"""
Ingrese el numero de serial ( Si no tiene, presione solo enter ): """)
                if NroSerial == "":
                    nuevoActivo["NroSerial"] = "Sin serial "
                if not nuevoActivo.get("NroSerial"):
                    if re.match(r'^[A-Z0-9\-_]+$', NroSerial) is not None:
                        if getNroSerial(NroSerial):
                            raise Exception("Serial ya existente.")
                        else:
                            nuevoActivo["NroSerial"] = NroSerial
                    else:
                        raise Exception("Serial no valido, recuerde que las letras deben ser mayusculas.")
                

            if not nuevoActivo.get("CodCampus"):
                codCampus = input(f"""
Ingrese el codigo Campus: """)
                if re.match(r'^[A-Z0-9\-_]+$', codCampus) is not None:
                    if getCodCampus(codCampus):
                        raise Exception("Codigo ingresado ya existente.")
                    else:
                        nuevoActivo["CodCampus"] = codCampus
                else:
                    raise Exception("Codigo no valido, recuerde que todas las letras deben ser mayusculas.")
                

            if not nuevoActivo.get("NroFormulario"):
                NroForm = input(f"""
Ingrese el numero del formulario: """)
                if re.match(r'^\d{9}$', NroForm) is not None:
                    asd = int(NroForm)
                    if getNroFormu(asd):
                        raise Exception("Numero ingresado ya existente.")
                    else:
                        nuevoActivo["NroFormulario"] = asd
                else:
                    raise Exception("Numero no valido, recuerde solo escribir 9 digitos numericos.")


            if not nuevoActivo.get("Nombre"):
                Nombre = input(f"""
Ingrese el nombre del activo: """)
                nuevoActivo["Nombre"] = Nombre


            if not nuevoActivo.get("Proveedor"):
                nuevoActivo["Proveedor"] = "Compumax Computer "


            if not nuevoActivo.get("EmpresaResponsable"):
                nuevoActivo["EmpresaResponsable"] = "Campuslands"


            if not nuevoActivo.get("idMarca"):
                print(f"""
Marcas: """)
                data = getMarcasData()
                for val in data:
                    print(f"{val['id']}. {val['Nombre']}")
                opcion = input(f"""
Seleccione una opcion: """)
                ids = list(val["id"] for val in data)
                if opcion not in ids:
                    raise Exception("Seleccion no valida")
                else:
                    nuevoActivo["idMarca"] = opcion
        

            if not nuevoActivo.get("idCategoria"):
                print(f"""
Categorias: """)
                data = getCategoriaData()
                for val in data:
                    print(f"{val['id']}. {val['Nombre']}")
                opcion = input(f"""
Seleccione una opcion: """)
                ids = list(val["id"] for val in data)
                if opcion not in ids:
                    raise Exception("Seleccion no valida")
                else:
                    nuevoActivo["idCategoria"] = opcion      
            

            if not nuevoActivo.get("idTipo"):
                print(f"""
Tipos de activos: """)
                data = getTipoData()
                for val in data:
                    print(f"{val['id']}. {val['Nombre']}")
                opcion = input(f"""
Seleccione una opcion: """)
                ids = list(val["id"] for val in data)
                if opcion not in ids:
                    raise Exception("Seleccion no valida")
                else:
                    nuevoActivo["idTipo"] = opcion

            if not nuevoActivo.get("ValorUnitario"):
                ValorUnitario = input(f"""
Ingrese el valor Unitario del activo: """)
                if re.match(r'^\d+$', ValorUnitario) is not None:
                    nuevoActivo["ValorUnitario"] = ValorUnitario
                else:
                    raise Exception("Ingrese solo digitos numericos.")


            if not nuevoActivo.get("idEstado"):
                nuevoActivo["idEstado"] = "0"


            if not nuevoActivo.get("historialActivos"):
                nuevoActivo["historialActivos"] = []


            if not nuevoActivo.get("asignaciones"):
                nuevoActivo["asignaciones"] = []


            ActivoLista = [nuevoActivo]
            print(tabulate(ActivoLista, headers="keys", tablefmt="rounded_grid"))
            print(f"""
¿Esta seguro que desea agregar el activo nuevo?
    1. Si
    2. Cancelar""")
            
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                requests.post("http://154.38.171.54:5502/activos", data=json.dumps(nuevoActivo, indent=4).encode("UTF-8"))
                print(f"""
Activo agregado correctamente.""")
                input(f"""
Presione enter para continuar.""")
                break
            elif opcion == "2":
                break
            else:
                raise Exception("Seleccion no valida.")


        except Exception as error:
            print(error)

##   EDITAR ACTIVO   ##
def editarActivo():
    id = input(f"""
Ingrese el id del activo que desea modificar: """)
    data = getActivosID(id)
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
                    if modificacion == "NroItem" or modificacion == "CodTransaccion" or modificacion == "NroFormulario":
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
            requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
            print(f"""
Activo modificado correctamente.""")
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

##   ELIMINAR ACTIVO ( DAR DE BAJA )   ##
def deleteActivo():
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
                    data[0]["idEstado"] = "2"
                    requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                    print(f"""
Activo dado de baja correctamente.""")
                    input(f"""
Presione enter para continuar.""")
                    break
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

######################   FILTROS   ######################
def getActivoPorId(id):
    activo = list()
    for val in getActivosData():
        if val.get("id") == id:
            activo.append({
                "id": val.get("id"),
                "Numero Item": val.get("NroItem"),
                "Numero Serial": val.get("NroSerial"),
                "Codigo Campus": val.get("CodCampus"),
                "NroFormulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "ID marca": val.get("idMarca"),
                "ID Categoria": val.get("idCategoria"),
                "ID tipo": val.get("idTipo"),
                "ID estado": val.get("idEstado"),
                "Valor Unitario": val.get("ValorUnitario"),
            })
    return activo

def getActivoPorNombre(nombre):
    activo = list()
    for val in getActivosData():
        if val.get("Nombre") == nombre:
            activo.append({
                "id": val.get("id"),
                "Numero Item": val.get("NroItem"),
                "Numero Serial": val.get("NroSerial"),
                "Codigo Campus": val.get("CodCampus"),
                "NroFormulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "ID marca": val.get("idMarca"),
                "ID Categoria": val.get("idCategoria"),
                "ID tipo": val.get("idTipo"),
                "ID estado": val.get("idEstado"),
                "Valor Unitario": val.get("ValorUnitario"),
            })
    return activo

def getActivoPorNroSerial(NroSerial):
    activo = list()
    for val in getActivosData():
        if val.get("NroSerial") == NroSerial:
            activo.append({
                "id": val.get("id"),
                "Numero Item": val.get("NroItem"),
                "Numero Serial": val.get("NroSerial"),
                "Codigo Campus": val.get("CodCampus"),
                "NroFormulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "ID marca": val.get("idMarca"),
                "ID Categoria": val.get("idCategoria"),
                "ID tipo": val.get("idTipo"),
                "ID estado": val.get("idEstado"),
                "Valor Unitario": val.get("ValorUnitario"),
            })
    return activo

def getActivoPorCodCampus(CodCampus):
    activo = list()
    for val in getActivosData():
        if val.get("CodCampus") == CodCampus:
            activo.append({
                "id": val.get("id"),
                "Numero Item": val.get("NroItem"),
                "Numero Serial": val.get("NroSerial"),
                "Codigo Campus": val.get("CodCampus"),
                "NroFormulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "ID marca": val.get("idMarca"),
                "ID Categoria": val.get("idCategoria"),
                "ID tipo": val.get("idTipo"),
                "ID estado": val.get("idEstado"),
                "Valor Unitario": val.get("ValorUnitario"),
            })
    return activo

def getActivoPorNroFormulario(NroFormulario):
    activo = list()
    for val in getActivosData():
        if val.get("NroFormulario") == NroFormulario:
            activo.append({
                "id": val.get("id"),
                "Numero Item": val.get("NroItem"),
                "Numero Serial": val.get("NroSerial"),
                "Codigo Campus": val.get("CodCampus"),
                "NroFormulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "ID marca": val.get("idMarca"),
                "ID Categoria": val.get("idCategoria"),
                "ID tipo": val.get("idTipo"),
                "ID estado": val.get("idEstado"),
                "Valor Unitario": val.get("ValorUnitario"),
            })
    return activo

def getActivoPorNroItem(NroItem):
    activo = list()
    for val in getActivosData():
        if val.get("NroItem") == NroItem:
            activo.append({
                "id": val.get("id"),
                "Numero Item": val.get("NroItem"),
                "Numero Serial": val.get("NroSerial"),
                "Codigo Campus": val.get("CodCampus"),
                "NroFormulario": val.get("NroFormulario"),
                "Nombre": val.get("Nombre"),
                "Proveedor": val.get("Proveedor"),
                "Empresa Responsable": val.get("EmpresaResponsable"),
                "ID marca": val.get("idMarca"),
                "ID Categoria": val.get("idCategoria"),
                "ID tipo": val.get("idTipo"),
                "ID estado": val.get("idEstado"),
                "Valor Unitario": val.get("ValorUnitario"),
            })
    return activo

##   BUSCAR ZONA   ##
def menuBuscarActivo():
    while True:
        try:
            os.system("clear")
            print(f"""
    ____                                ___        __  _                 
   / __ )__  ________________ ______   /   | _____/ /_(_)   ______  _____
  / __  / / / / ___/ ___/ __ `/ ___/  / /| |/ ___/ __/ / | / / __ \/ ___/
 / /_/ / /_/ (__  ) /__/ /_/ / /     / ___ / /__/ /_/ /| |/ / /_/ (__  ) 
/_____/\__,_/____/\___/\__,_/_/     /_/  |_\___/\__/_/ |___/\____/____/  
                                                                                                                                    
                                                                            
OPCIONES:
    1. Buscar activo segun su id.
    2. Buscar activo segun su nombre.
    3. Buscar activo segun su numero serial.
    4. Buscar activo segun su codigo Campus.
    5. Buscar activo segun su numero de formulario.
    6. Buscar activo segun su numero de item.
    7. Regresar. """)
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                id = input(f"""
Escriba el id: """)
                print(tabulate(getActivoPorId(id), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "2":
                nombre = input(f"""
Escriba el nombre: """)
                print(tabulate(getActivoPorNombre(nombre), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "3":
                Nro = input(f"""
Escriba el numero de serial: """)
                print(tabulate(getActivoPorNroSerial(Nro), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "4":
                CodCampus = input(f"""
Escriba el codigo campus: """)
                print(tabulate(getActivoPorCodCampus(CodCampus), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "5":
                NroFormulario = int(input(f"""
Escriba el numero de formulario: """))
                print(tabulate(getActivoPorNroFormulario(NroFormulario), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "6":
                NroItem = int(input(f"""
Escriba el numero de item: """))
                print(tabulate(getActivoPorNroItem(NroItem), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "7":
                break
            else:
                raise Exception("Opcion no valida.") 

        except Exception as error:
            print(error)

##   MENU DE ACTIVOS   ##
def menuActivos():
    while True:
        try:
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
    5. REGRESAR AL MENU PRINCIPAL           """)
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                postActivos()
            elif opcion == "2":
                editarActivo()
            elif opcion == "3":
                deleteActivo()            
            elif opcion == "4":
                menuBuscarActivo()
            elif opcion == "5":
                break
            else:
                raise Exception ("Opcion no valida.")
        
        except Exception as error:
            print(error)