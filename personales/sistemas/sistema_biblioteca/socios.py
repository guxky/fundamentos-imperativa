""""
representaciond e socio s
"""
from validaciones import es_nombre_valido

socios = [
    {"id": "1", "Nombre": "Ana"},
    {"id": "2", "Nombre": "Carlos"},
    {"id": "3", "Nombre": "Beto"},
    {"id": "4", "Nombre": "Diana Maria"},
]

def registrar_socio(socios: list, id: str, nombre: str)->str:
    acum = ""
    if es_nombre_valido(nombre):        
        socio = {"id": id, "Nombre": nombre}
        socios.append(socio)
        acum = f'\nSocio registrado: {nombre} (ID: {id})'
        return acum
    else:
        acum = f'\nEl nombre {nombre} no es valido'
        return acum  

def buscar_socio(socios: list, id: str)-> str:
    acum = ""
    for socio in socios:
        if(socio["id"] == id):
            acum = f'\nNombre: {socio["Nombre"]}\nID: {id}'
            return acum
    else:
        acum =f'\nNo se encontro ningun socio con el ID: {id}'
        return acum

