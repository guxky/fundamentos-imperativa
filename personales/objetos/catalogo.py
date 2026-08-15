from libro import Libro
import validaciones as vali

class Catalogo:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro_isbn(self, isbn):
        if not vali.es_isbn_valido(isbn):
            return f'\n{isbn} No es valido'
        
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        else: 
            return f'\nNo se encontro ninguno libro con isbn: {isbn} en el catalogo'
        

    def buscar_libro_autor(self, autor):
        if not vali.es_nombre_valido(autor):
            return f'\n{autor} No es un nombre valido'
        
        catalogos_autor = Catalogo()
        for libro in self.catalogo:
            if libro.autor == autor:
                catalogos_autor.agregar_libro(libro)
        return catalogos_autor

    def __str__(self):
        acum = ""
        for libro in self.catalogo:
            acum += f"\n{libro}"
        return acum
