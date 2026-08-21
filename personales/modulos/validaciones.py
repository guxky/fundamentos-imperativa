def es_calificacion_valida(calificacion: float) -> bool:
    return 0<=calificacion<= 100

def es_nombre_valido(nombre: str) -> bool:
    if len(nombre) == 0:
        return False
    return True

