from validaciones import es_isbn_valido
from decoradores import contar_prestamos, registrar_operacion


@contar_prestamos
@registrar_operacion
def prestar_libro(catalogo: list, socios: list, isbn: str, id_socio: str)-> str:
    acum = ""
    if not es_isbn_valido(isbn):
        acum = f"\nEl formato del ISBN no es válido."
        return acum

    if not any(u["id"] == id_socio for u in socios):
        acum =  f"\nEl socio con ID '{id_socio}' no está registrado."
        return acum

    socio_actual = next(s for s in socios if s["id"] == id_socio)

    for libro in catalogo:
        if libro["ISBN"] == isbn:

            if libro["Disponible"]:
                libro["Disponible"] = False
                acum = f'\nPrestamo registrado: {libro["Titulo"]} -> {socio_actual["Nombre"]}'
                return acum
            
            elif id_socio in libro["Cola de espera"]:
                acum = f'\n{socio_actual["Nombre"]} ya esta en la lista de espera'
                return acum

            else:
                libro["Cola de espera"].append(id_socio)
                acum = f'\n{libro["Titulo"]} no esta disponible, {socio_actual["Nombre"]} se agrego a la lista de espera'
                return acum
            
    else:
        acum = f'\nEl libro con ISBN {isbn} no existe en el catalogo'
        return acum

@registrar_operacion
def devolver_libro(catalogo: list, isbn: str) -> str:
    acum = ""
    if not es_isbn_valido(isbn):
            acum = f"\nEl formato del ISBN no es válido."
            return acum
    
    for libro in catalogo:
         if libro["ISBN"] == isbn:
            if not libro["Cola de espera"] and not libro["Disponible"]:
                libro["Disponible"] = True
                acum = f'\nLibro devuelto: "{libro["Titulo"]}". Ahora esta disponible'
                return acum

            if libro["Cola de espera"]:
                actual = libro["Cola de espera"].popleft()
                acum += f'\nLibro devuelto: {libro["Titulo"]}'
                acum +=f'\nLibro asignado automaticamente al siguiente usuario'
                return acum

            if libro["Disponible"]:
                acum += f'\nEl libro ya se encuentra disponible'
                return acum
    else:
        acum += f'\nEl libro con ISBN: {isbn} No se encuentra en el catalogo'
        return acum
            
                
