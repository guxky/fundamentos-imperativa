class Socios:
    def __init__(self):
        self.socios = []

    def registrar_socio(self, socio):
        self.socios.append(socio)

    def buscar_socio(self, id):
        socio = next((s for s in self.socios if s.id == id), None)
        if socio is None:
            return f'\nNo se encontro ningun socio con id: {id}'
        return socio.nombre

    
