from collections import deque
import validaciones as vali

class Libro:
    
    def __init__(self, isbn, titulo, autor):
        if not vali.es_isbn_valido(isbn):
            raise ValueError(f"\nEl ISBN '{isbn}' no es valido")

        if not vali.es_nombre_valido(autor):
            raise ValueError(f"\nEl nombre del autor no es valido")
        
        if not titulo: raise ValueError{f"\nEl titulo no puede ir vacio"}
        
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponibilidad = True
        self.cola_espera = deque()

    def get_isbn(self):
        return self.isbn

    def get_autor(self):
        return self.autor

    def set_disponibilidad(self, estado):
        self.disponibilidad = estado

    def __str__(self):
        acum = f'{self.isbn}\t{self.titulo}\t{self.autor}'
        return acum

    