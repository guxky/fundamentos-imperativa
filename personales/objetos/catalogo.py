from libro import Libro

class Catalogo:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro_isbn(self, isbn):
        for libro in self.catalogo:
            if Libro.autor() == isbn:
                return libro
            else: 
                return f'\nNo se encontro ninguno libro con isbn: {isbn} en el catalogo'

    def buscar_libro_autor(self, autor):
        catalogos_autor = Catalogo()
        for libro in self.catalogo:
            if libro.autor() == autor:
                catalogos_autor.agregar_libro(libro)


    def __str__(self):
        acum = ""
        for libro in self.catalogo:
            acum += f"\n{libro}"
        return acum

l1 = Libro(123, "hola", "manuela")
c = Catalogo()
c.agregar_libro(l1)
print(c)