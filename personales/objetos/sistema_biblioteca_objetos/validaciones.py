import re

def es_isbn_valido(isbn):
    return bool(re.fullmatch(r"\d{13}", isbn))

def es_nombre_valido(nombre):
    return (bool(re.fullmatch(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+", nombre)))

def existe_id(socios, id):
    s = next((s for s in socios.socios if s.id == id), None)
    return s
