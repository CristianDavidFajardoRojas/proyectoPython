import os
import requests
from tabulate import tabulate 

def getActivosData():
    peticion = requests.get("http://154.38.171.54:5502/activos")
    data = peticion.json()
    return data

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
6. REGRESAR AL MENU PRINCIPAL""")
        opcion = input(f"""
Seleccione una opcion: """)
        if opcion == "1":
            print(tabulate(getActivoPorNombre(), headers="keys", tablefmt="rounded_grid"))
            input(f"""
Presione enter para continuar.""")