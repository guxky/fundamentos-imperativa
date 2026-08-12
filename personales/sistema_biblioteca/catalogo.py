from validaciones import es_isbn_valido,es_nombre_valido
from collections import deque

"""
representacion de un almacen de libros; los librros son diccionarios
"""
catalogo_libros = [
    {"ISBN": "9780307474723", "Titulo": "Cien años de soledad", "Autor": "Gabriel Garcia Marquez", "Disponible": True, "Cola de espera": deque()},
    {"ISBN": "9780061120084", "Titulo": "El amor en los tiempos del colera", "Autor": "Gabriel Garcia Marquez", "Disponible": True, "Cola de espera": deque()},
    {"ISBN": "9788437604947", "Titulo": "Rayuela", "Autor": "Julio Cortazar", "Disponible": True, "Cola de espera": deque()},
    {"ISBN": "9780143039433", "Titulo": "Ficciones", "Autor": "Jorge Luis Borges", "Disponible": True, "Cola de espera": deque()},
    {"ISBN": "9780307387899", "Titulo": "Pedro Paramo", "Autor": "Juan Rulfo", "Disponible": True, "Cola de espera": deque()},
]

"""
funcion que recibe la representacind e un catalogo y agrega un libro con su debida representacion
"""

def agregar_libro(catalogo_libros: list, isbn: str, titulo: str, autor: str) -> str:
    acum = ""
    if es_isbn_valido(isbn):
        libro = {"ISBN": isbn, "Titulo": titulo, "Autor": autor, "Disponible": True, "Cola de espera": deque()}
        catalogo_libros.append(libro)
        acum = f'\nLibro agregado: "{titulo}" (ISBN: {isbn})'
        return acum
    else:
        acum = f'\nEl ISBN {isbn} NO es valido'
        return acum


def buscar_libro_isbn(catalogo_libros: list, isbn: str) -> str:
    acum = ""
    if es_isbn_valido(isbn):
        for libro in catalogo_libros:
            if(isbn == libro["ISBN"]):
                acum = f'\nTitulo: {libro["Titulo"]} \nAutor: {libro["Autor"]}'
                return acum
        else:
            acum = f'\nNo se encontro ningun libro con ISBN {isbn}'
            return acum
    else:
        acum = f'\n{isbn} No es un ISBN valido'
        return acum

def buscar_libros_autor(catalogo_libros: list, autor: str) -> str:
    acum = f"\nLibros de {autor}"
    existe = False
    if es_nombre_valido(autor):
        for libro in catalogo_libros:
            if libro["Autor"] == autor:
                acum += f'\n-{libro["Titulo"]}'
                existe = True

        if not existe:
            acum = f'\nNo se encontro libro con autor: {autor}'
            return acum
    else:
        acum = f'\nNo es un nombre valido'
        return acum
    
    return acum    


def mostrar_catalogo(catalogo_libros: list) -> str:
    acum = "\nCatalogo completo:"
    catalogo_ordenado = sorted(catalogo_libros, key=lambda x: x["Autor"])
    if not catalogo_ordenado: 
        acum += f'\nEl catalogo esta vacio'
        return acum
    else:
        for libro in catalogo_ordenado:
            acum += f'\n{libro["ISBN"]} - {libro["Titulo"]}'

    return acum