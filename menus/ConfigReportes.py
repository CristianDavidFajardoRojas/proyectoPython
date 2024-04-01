import os
import requests
from tabulate import tabulate 
from datetime import datetime

def limpiar_pantalla():
    sistema_operativo = os.name
    if sistema_operativo == "posix":  
        os.system("clear")
    elif sistema_operativo == "nt":  
        os.system("cls")
    else:
        print("Sistema operativo no compatible")

def getActivosData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

def getCategoriaData():
    peticion = requests.get("http://154.38.171.54:5502/categoriaActivos")
    data = peticion.json()
    return data

def getActivoslID(id):
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return [peticion.json()] if peticion.ok else []

######################   FILTROS   ######################
def getActivoPorNombre():
    activo = list()
    for val in getActivosData():
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

def getActivoPorCategoria(id):
    activo = list()
    for val in getActivosData():
        if val.get("idCategoria") == id:
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

def getActivoDadoDeBaja():
    activo = list()
    for val in getActivosData():
        if val.get("idEstado") == "2":
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

def getDataAsiganciones():
    result = []
    for val in getActivosData():
        if val.get("asignaciones"):
            diccitionarioss = val['asignaciones'][0]
            diccitionarioss["ID Activo"] = val.get("id")
            diccitionarioss["Nombre del Activo"] = val.get("Nombre")
            result.append(diccitionarioss)
    return result

def getDataHistoriales():
    id = input("Escriba el ID del activo que desea conocer el historial: ")
    result = []
    for val in getActivoslID(id):
        if val.get("historialActivos"):
            for asd in val['historialActivos']:
                diccitionarioss = asd
                result.append(diccitionarioss)
    return result

def menuReportes():
    while True:
        try:
            limpiar_pantalla()
            print(f"""
    __  ___                    ____                        __           
   /  |/  /__  ____  __  __   / __ \___  ____  ____  _____/ /____  _____
  / /|_/ / _ \/ __ \/ / / /  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/
 / /  / /  __/ / / / /_/ /  / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  ) 
/_/  /_/\___/_/ /_/\__,_/  /_/ |_|\___/ .___/\____/_/   \__/\___/____/  
                                     /_/                                
                                                      

OPCIONES:
1. LISTAR TODOS LOS ACTIVOS
2. LISTAR ACTIVOS POR CATEGORIA
3. LISTAR ACTIVOS DADOS DE BAJA POR DAÑO
4. LISTAR ACTIVOS Y ASIGNACION
5. LISTAR HISTORIAL DE MOV. DE ACTIVO
6. REGRESAR AL MENU PRINCIPAL""")
            opcion = input(f"""
Seleccione una opcion: """)
            if opcion == "1":
                print(tabulate(getActivoPorNombre(), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "2":
                data = getCategoriaData()
                print(f"""
CATEGORIAS: """)
                for val in data:
                    print(f"{val['id']}. {val['Nombre']}")
                categoria = input(f"""
Seleccione una opcion: """) 
                if categoria not in list(val["id"] for val in data):
                    raise Exception("Opcion no valida")
                else:
                    print(tabulate(getActivoPorCategoria(categoria), headers="keys", tablefmt="rounded_grid"))
                    input(f"""
Presione enter para continuar.""")
                
            elif opcion == "3":
                print(tabulate(getActivoDadoDeBaja(), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
                
            elif opcion == "4":
                print(tabulate(getDataAsiganciones(), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "5":
                print(tabulate(getDataHistoriales(), headers="keys", tablefmt="rounded_grid"))
                input(f"""
Presione enter para continuar.""")
            elif opcion == "6":
                break
                


        except Exception as error:
            print(error)