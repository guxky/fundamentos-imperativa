from collections import deque
import validaciones as vali

class Libro:
    
    def __init__(self, isbn, titulo, autor):
        if not vali.es_isbn_valido(isbn):
            raise ValueError(f"\nEl ISBN '{isbn}' no es valido")

        if not vali.es_nombre_valido(autor):
            raise ValueError(f"\nEl nombre del autor no es valido")
        
        if not titulo: 
            raise ValueError(f"\nEl titulo no puede ir vacio")
        
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._disponibilidad = True
        self._prestado_a = None
        self._cola_espera = deque()

    @property
    def isbn(self):
        return self._isbn

    @property
    def titulo (self):
        return self._titulo

    @property
    def autor(self):
        return self._autor
    
    @property
    def disponibilidad(self):
        return self._disponibilidad

    @property
    def prestado_a(self):
        return self._prestado_a
    
    @property
    def cola_espera(self):
        return self._cola_espera

    @disponibilidad.setter
    def disponibilidad(self, estado):
        self._disponibilidad = estado

    @prestado_a.setter
    def prestado_a(self, socio):
        self._prestado_a = socio


    def __str__(self):
        acum = f'{self.isbn}\t{self.titulo}\t{self.autor}'
        return acum

    