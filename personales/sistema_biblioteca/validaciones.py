ISBN = 13


def es_isbn_valido(isbn: str) -> bool:
    if isbn.isdigit() and len(isbn) == ISBN:
        return True
    else:
        return False

def es_nombre_valido(nombre: str) -> bool:
    if nombre.replace(" ", "").isalpha():
        return True
    else:
        return False