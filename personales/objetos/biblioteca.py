from catalogo import Catalogo
from socios import Socios
from libro import Libro
from socio import Socio
from validaciones import es_isbn_valido
from collections import deque
from decoradores import contar_prestamos, registrar_operacion

class Biblioteca:
    def __init__(self, catalogo, socios):
        self.catalogo = catalogo
        self.socios = socios

    @contar_prestamos
    @registrar_operacion    
    def prestar_libro(self, id, isbn):
        if not es_isbn_valido(isbn):
            raise ValueError(f'\n{isbn} es un isbn invalido')

        s = next((s for s in self.socios if s.id == id), None)
        l = next((l for l in self.catalogo if l.isbn == isbn), None)

        if s is None:
            raise ValueError(f'\nEl socio no se encuentr {s.nombre} no se encuentra en el catalogo')
        if l is None:
            raise ValueError(f'\nEl libro {l.titulo} no se encuentra registrado en el catalogo')

        if l.disponibilidad:
            l.pretado_a = s
            l.disponibilidad = False
            return f'\nSe presto el libro {l.titulo} a {s.nombre}'

        elif s in l.cola_espera:
            return f'\n{s.nombre} ya se encuentra en la cola de espera'

        else:
            l.cola_espera.append(s)
            return f'\n{s.nombre} se agrego a la cola de espera'

    @registrar_operacion    
    def devolver_libro(self, isbn):
        if not es_isbn_valido(isbn):
            raise ValueError(f'\n{isbn} es un isbn invalido')

        l = next((l for l in self.catalogo if l.isbn == isbn), None)

        if l.disponibilidad:
            return f'\nEl libro {l.titulo} ya se encuentra disponible'

        elif not l.cola_espera:
            l.prestado_a = None
            l.disponibilidad = True
            return f'\nSe devolvio el libro, se encuentra disponible'

        else:
            l.prestado_a = l.cola_espera.popleft()
            return f'\nSe devolvio el libro \nSe asigno el libro {l.titulo} a {l.pestado_a}'

        

        
    