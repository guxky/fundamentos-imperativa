class Socio:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

