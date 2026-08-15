def contar_prestamos(funcion):
    def envoltura(*args, **kwargs):
        envoltura.contador+= 1
        print(f'\nPrestamo numero: {envoltura.contador}')
        return funcion(*args, **kwargs)
    envoltura.contador = 0
    return envoltura

def registrar_operacion(funcion):
    def envoltura(*args, **kwargs):
        print(f'\n{funcion.__name__} Ejecutada con {args[2:5]}')
        return funcion(*args, **kwargs)
    return envoltura
